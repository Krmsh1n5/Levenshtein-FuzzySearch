"""
Tourism Location Search System
Hybrid fuzzy matching for travel/navigation apps
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from optimizations.bk_tree import BKTree
from algorithms.levenshtein import levenshtein_distance
from techniques.phonetic_search import PhoneticSearch
from techniques.ngram_search import NGramSearch
from collections import defaultdict

class TourismSearchEngine:
    def __init__(self, locations):
        self.locations = locations
        
        # Initialize BK-Tree with empty word list and distance function
        self.bk_tree = BKTree([], levenshtein_distance)  # Fixed initialization
        self.phonetic = PhoneticSearch(locations)
        self.ngram = NGramSearch(locations, n=3)
        
        # Populate BK-Tree with locations
        for loc in locations:
            self.bk_tree.insert(loc)
            
        self.weights = {
            'levenshtein': 0.6,
            'phonetic': 0.3,
            'ngram': 0.1
        }



    def search(self, query, max_results=5):
        """Main interface for tourism queries"""
        # Get results from each technique
        lev_matches = self.bk_tree.search(query, 2)
        pho_matches = self.phonetic.search(query)
        ngram_matches = self.ngram.search(query)
        
        # Combine scores
        scores = defaultdict(float)
        for word, dist in lev_matches:
            scores[word] += self.weights['levenshtein'] * (1 - dist/10)
            
        for word, score in pho_matches:
            scores[word] += self.weights['phonetic'] * score
            
        for word, score in ngram_matches:
            scores[word] += self.weights['ngram'] * score
            
        # Return top matches
        return sorted(scores.items(), key=lambda x: -x[1])[:max_results]