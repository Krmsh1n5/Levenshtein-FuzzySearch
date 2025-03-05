"""
Unit Tests for Optimization Techniques

This module provides unit tests for the optimization techniques (BK-tree, parallel processing, ANN search).
"""
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/optimizations')))

from optimizations.bk_tree import BKTree
from optimizations.parallel_processing import parallel_fuzzy_search
from optimizations.ann_search import build_faiss_index, ann_search

# Add the path to the src/algorithms directory for levenshtein_distance
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/algorithms')))
from Levenshtein import distance as levenshtein_distance

class TestOptimizations(unittest.TestCase):
    # BK-Tree Tests
    def test_bk_tree_exact_match(self):
        tree = BKTree(levenshtein_distance)
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        for target in targets:
            tree.insert(target)
        matches = tree.search("apple", 0)  
        self.assertIn(("apple", 0), matches)

    def test_bk_tree_typo(self):
        tree = BKTree(levenshtein_distance)
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        for target in targets:
            tree.insert(target)
        matches = tree.search("aple", 2)
        self.assertIn(("apple", 1), matches)

    def test_bk_tree_no_match(self):
        tree = BKTree(levenshtein_distance)
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        for target in targets:
            tree.insert(target)
        matches = tree.search("xyz", 2)  
        self.assertEqual(len(matches), 0)

    # Parallel Processing Tests
    def test_parallel_processing_exact_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = parallel_fuzzy_search("apple", targets, threshold=0) 
        self.assertIn(("apple", 0), matches)

    def test_parallel_processing_no_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        matches = parallel_fuzzy_search("xyz", targets, threshold=2)  
        self.assertEqual(len(matches), 0)

    # ANN Search Tests
    def test_ann_search_exact_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        index, embeddings = build_faiss_index(targets)
        matches = ann_search("apple", index, targets, k=3)
        self.assertIn("apple", [match[0] for match in matches])

    def test_ann_search_typo(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        index, embeddings = build_faiss_index(targets)
        matches = ann_search("aple", index, targets, k=3, distance_threshold=1.5) 
        self.assertIn("apple", [match[0] for match in matches]) 

    def test_ann_search_empty_targets(self):
        targets = []
        index, embeddings = build_faiss_index(targets)
        matches = ann_search("apple", index, targets, k=3)
        self.assertEqual(len(matches), 0) 

    def test_ann_search_no_match(self):
        targets = ["apple", "banana", "orange", "grape", "pineapple"]
        index, embeddings = build_faiss_index(targets)
        matches = ann_search("xyz", index, targets, k=3, distance_threshold=0.1)  # Use a small threshold
        self.assertEqual(len(matches), 0)  

    # Edge Cases
    def test_bk_tree_empty_targets(self):
        tree = BKTree(levenshtein_distance)
        matches = tree.search("apple", 2) 
        self.assertEqual(len(matches), 0)

    def test_parallel_processing_empty_targets(self):
        targets = []
        matches = parallel_fuzzy_search("apple", targets, threshold=2)
        self.assertEqual(len(matches), 0)

    def test_ann_search_empty_targets(self):
        targets = []
        index, embeddings = build_faiss_index(targets)
        matches = ann_search("apple", index, targets, k=3) 
        self.assertEqual(len(matches), 0)

if __name__ == "__main__":
    unittest.main()