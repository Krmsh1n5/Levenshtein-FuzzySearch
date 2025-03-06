"""
N-Gram Based Fuzzy Search

This module provides an implementation of n-gram based fuzzy search, which compares
strings based on overlapping n-grams (substrings of length n).

References:
- Cavnar, W. B., & Trenkle, J. M. (1994). "N-Gram-Based Text Categorization".
  Proceedings of SDAIR-94, 161-175.
- Jurafsky, D., & Martin, J. H. (2023). "Speech and Language Processing".
  Stanford University. https://web.stanford.edu/~jurafsky/slp3/
"""

from collections import defaultdict, Counter
from nltk.util import ngrams

class NGramSearch:
    def __init__(self, targets, n=2, preprocess=True):
        """
        Initialize search engine with precomputed n-gram profiles
        
        Args:
            targets (list): List of strings to search in
            n (int): N-gram size
            preprocess (bool): Enable lowercase/normalization
        """
        self.n = n
        self.preprocess = preprocess
        self.target_profiles = self._create_profiles(targets)
        
    def _normalize(self, s):
        """Uniform string preprocessing"""
        return s.lower().strip() if self.preprocess else s

    def _create_profiles(self, targets):
        """Precompute n-gram frequency profiles"""
        profiles = {}
        for target in targets:
            normalized = self._normalize(target)
            target_ngrams = list(ngrams(normalized, self.n))
            profiles[target] = {
                'counts': Counter(target_ngrams),
                'total': len(target_ngrams)
            }
        return profiles

    def _ngram_similarity(self, query_profile, target_profile):
        """
        Combined similarity score using:
        - Jaccard similarity (set intersection/union)
        - Containment coefficient (query coverage)
        """
        query_counts = query_profile['counts']
        target_counts = target_profile['counts']
        
        intersection = sum((query_counts & target_counts).values())
        union = sum((query_counts | target_counts).values())
        containment = intersection / query_profile['total'] if query_profile['total'] > 0 else 0
        
        jaccard = intersection / union if union > 0 else 0
        return 0.7*jaccard + 0.3*containment  # Weighted combination

    def search(self, query, top_k=5, min_score=0.1):
        """
        Find top matches with combined scoring
        
        Args:
            query (str): Search string
            top_k (int): Maximum results to return
            min_score (float): Minimum similarity threshold
            
        Returns:
            list: Sorted matches as (target, score)
        """
        normalized_query = self._normalize(query)
        query_ngrams = list(ngrams(normalized_query, self.n))
        query_profile = {
            'counts': Counter(query_ngrams),
            'total': len(query_ngrams)
        }
        
        scores = []
        for target, profile in self.target_profiles.items():
            score = self._ngram_similarity(query_profile, profile)
            if score >= min_score:
                scores.append((target, score))
                
        # Sort by score descending, then alphabetically
        return sorted(scores, key=lambda x: (-x[1], x[0]))[:top_k]