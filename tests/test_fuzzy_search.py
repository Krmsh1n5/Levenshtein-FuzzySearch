"""
Unit Tests for Fuzzy Search Techniques

This module provides comprehensive unit tests for the fuzzy search techniques (n-gram, phonetic, ML-based),
covering edge cases, real-world scenarios, and all possible types of string comparisons.
"""

import unittest
import sys
import os

# Add the path to the src/techniques directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/techniques')))

# Import the functions directly from the files
from ngram_search import ngram_fuzzy_search
from phonetic_search import phonetic_fuzzy_search
from ml_search import ml_fuzzy_search, hybrid_fuzzy_search

class TestFuzzySearch(unittest.TestCase):
    # N-Gram Fuzzy Search Tests
    def test_ngram_fuzzy_search_exact_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = ngram_fuzzy_search("apple", targets, n=2, threshold=0.5)
        self.assertIn("apple", [match[0] for match in matches])

    def test_ngram_fuzzy_search_typo(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = ngram_fuzzy_search("aple", targets, n=2, threshold=0.5)
        self.assertIn("apple", [match[0] for match in matches])

    def test_ngram_fuzzy_search_no_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = ngram_fuzzy_search("xyz", targets, n=2, threshold=0.5)
        self.assertEqual(len(matches), 0)

    # Phonetic Fuzzy Search Tests
    def test_phonetic_fuzzy_search_exact_match(self):
        targets = ["Robert", "Rupert", "Rob", "Robby", "Alice", "Bob"]
        matches = phonetic_fuzzy_search("Robert", targets)
        self.assertIn("Robert", matches)

    def test_phonetic_fuzzy_search_similar_names(self):
        targets = ["Robert", "Rupert", "Rob", "Robby", "Alice", "Bob"]
        matches = phonetic_fuzzy_search("Robert", targets)
        self.assertIn("Rupert", matches)

    def test_phonetic_fuzzy_search_no_match(self):
        targets = ["Robert", "Rupert", "Rob", "Robby", "Alice", "Bob"]
        matches = phonetic_fuzzy_search("XYZ", targets)
        self.assertEqual(len(matches), 0)

    def test_phonetic_fuzzy_search_unicode_names(self):
        targets = ["Jörg", "Jörgen", "George", "Georg"]
        matches = phonetic_fuzzy_search("Jörg", targets)
        self.assertIn("George", matches)

    # Machine Learning-Based Fuzzy Search Tests
    def test_ml_fuzzy_search_exact_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = ml_fuzzy_search("apple", targets, threshold=0.5)
        self.assertIn("apple", [match[0] for match in matches])

    def test_ml_fuzzy_search_typo(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = hybrid_fuzzy_search("aple", targets, ml_threshold=0.4, edit_threshold=2)
        self.assertIn("apple", matches)

    def test_ml_fuzzy_search_no_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = ml_fuzzy_search("xyz", targets, threshold=0.5)
        self.assertEqual(len(matches), 0)

    def test_ml_fuzzy_search_real_world_typos(self):
        targets = ["restaurant", "restuarant", "restaraunt"]
        matches = ml_fuzzy_search("restuarant", targets, threshold=0.5)
        self.assertIn("restaurant", [match[0] for match in matches])

    # Edge Cases
    def test_ngram_fuzzy_search_empty_targets(self):
        targets = []
        matches = ngram_fuzzy_search("apple", targets, n=2, threshold=0.5)
        self.assertEqual(len(matches), 0)

    def test_phonetic_fuzzy_search_empty_targets(self):
        targets = []
        matches = phonetic_fuzzy_search("Robert", targets)
        self.assertEqual(len(matches), 0)

    def test_ml_fuzzy_search_empty_targets(self):
        targets = []
        matches = ml_fuzzy_search("apple", targets, threshold=0.5)
        self.assertEqual(len(matches), 0)

    # Real-World Scenarios
    def test_ngram_fuzzy_search_real_world_typos(self):
        targets = ["accommodation", "accomodation", "recommendation"]
        matches = ngram_fuzzy_search("accomodation", targets, n=2, threshold=0.5)
        self.assertIn("accommodation", [match[0] for match in matches])

    def test_phonetic_fuzzy_search_real_world_names(self):
        targets = ["Christopher", "Kristofer", "Jennifer", "Jenifer"]
        matches = phonetic_fuzzy_search("Christopher", targets)
        self.assertIn("Kristofer", matches)

    def test_ml_fuzzy_search_real_world_typos(self):
        targets = ["restaurant", "restuarant", "restaraunt"]
        matches = ml_fuzzy_search("restuarant", targets, threshold=0.5)
        self.assertIn("restaurant", [match[0] for match in matches])

if __name__ == "__main__":
    unittest.main()