"""
Phonetic Algorithms for Fuzzy Search

This module provides implementations of phonetic algorithms (Soundex, Metaphone)
for fuzzy search, which are useful for handling pronunciation-based errors.

References:
- Odell, M. K., & Russell, R. C. (1918). "Soundex Coding System".
  U.S. Patent No. 1,261,167.
- Philips, L. (1990). "Hanging on the Metaphone". Computer Language, 7(12), 39-44.
"""

from jellyfish import soundex, metaphone
from dataclasses import dataclass

@dataclass
class PhoneticConfig:
    soundex_weight: float = 0.6  
    metaphone_weight: float = 0.4  
    min_score: float = 0.3 
    normalize: bool = True
    metaphone_length: int = 4 

class PhoneticSearch:
    def __init__(self, targets, config=PhoneticConfig()):
        self.config = config
        self.targets = self._preprocess_targets(targets)
        
    def _preprocess(self, s):
        return s.lower().replace("-", " ").strip() if self.config.normalize else s

    def _preprocess_targets(self, targets):
        preprocessed = []
        for target in targets:
            processed = self._preprocess(target)
            preprocessed.append({
                'original': target,
                'soundex': soundex(processed),
                'metaphone': metaphone(processed)[:self.config.metaphone_length]
            })
        return preprocessed

    def _calculate_score(self, query_codes, target):
        score = 0.0
        
        # Soundex match
        if query_codes['soundex'] == target['soundex']:
            score += self.config.soundex_weight
            
        # Metaphone partial match
        q_meta = query_codes['metaphone']
        t_meta = target['metaphone']
        
        # Check prefix matching
        min_length = min(len(q_meta), len(t_meta))
        match_count = sum(1 for i in range(min_length) if q_meta[i] == t_meta[i])
        
        if min_length > 0:
            score += self.config.metaphone_weight * (match_count / min_length)
            
        return min(score, 1.0)

    def search(self, query, top_k=5):
        processed_query = self._preprocess(query)
        query_codes = {
            'soundex': soundex(processed_query),
            'metaphone': metaphone(processed_query)  # Removed max_length
        }
        
        scored_matches = []
        for target in self.targets:
            score = self._calculate_score(query_codes, target)
            if score >= self.config.min_score:
                scored_matches.append((target['original'], score))
                
        return sorted(scored_matches, key=lambda x: (-x[1], x[0]))[:top_k]