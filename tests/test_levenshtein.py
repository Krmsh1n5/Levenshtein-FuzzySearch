"""
Unit Tests for Levenshtein Distance (Library Implementation)

This module provides comprehensive unit tests for the Levenshtein distance function
from the `Levenshtein` library, covering edge cases, real-world scenarios, and all
possible types of string comparisons.
"""

import unittest
from Levenshtein import distance as levenshtein_distance

class TestLevenshteinDistance(unittest.TestCase):
    # Basic Tests
    def test_identical_strings(self):
        self.assertEqual(levenshtein_distance("kitten", "kitten"), 0)

    def test_one_edit(self):
        self.assertEqual(levenshtein_distance("kitten", "sitten"), 1) 
        self.assertEqual(levenshtein_distance("kitten", "kittens"), 1)  
        self.assertEqual(levenshtein_distance("kitten", "itten"), 1) 

    def test_multiple_edits(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)  

    def test_empty_string(self):
        self.assertEqual(levenshtein_distance("", "kitten"), 6)  
        self.assertEqual(levenshtein_distance("kitten", ""), 6)  

    # Case Sensitivity
    def test_case_sensitivity(self):
        self.assertEqual(levenshtein_distance("Kitten", "kitten"), 1)  
        self.assertEqual(levenshtein_distance("HELLO", "hello"), 5)  

    # Unicode and Special Characters
    def test_unicode_characters(self):
        self.assertEqual(levenshtein_distance("café", "cafe"), 1) 
        self.assertEqual(levenshtein_distance("こんにちは", "こんにちわ"), 1)  
        self.assertEqual(levenshtein_distance("straße", "strasse"), 2)

    def test_special_characters(self):
        self.assertEqual(levenshtein_distance("hello!", "hello?"), 1) 
        self.assertEqual(levenshtein_distance("hello#world", "hello@world"), 1)  

    # Real-World Scenarios
    def test_real_world_names(self):
        self.assertEqual(levenshtein_distance("Christopher", "Kristofer"), 4) 
        self.assertEqual(levenshtein_distance("Jennifer", "Jenifer"), 1) 

    def test_real_world_addresses(self):
        self.assertEqual(levenshtein_distance("123 Main St", "123 Main Street"), 4) 
        self.assertEqual(levenshtein_distance("Apt 4B", "Apartment 4B"), 6)  

    def test_real_world_typos(self):
        self.assertEqual(levenshtein_distance("accomodation", "accommodation"), 1) 
        self.assertEqual(levenshtein_distance("recieve", "receive"), 2) 

    # Long Strings
    def test_long_strings(self):
        str1 = "a" * 1000
        str2 = "b" * 1000
        self.assertEqual(levenshtein_distance(str1, str2), 1000)  

    # Mixed Cases
    def test_mixed_case_strings(self):
        self.assertEqual(levenshtein_distance("HelloWorld", "helloworld"), 2)
        self.assertEqual(levenshtein_distance("PythonCode", "pythoncode"), 2) 

    # Numbers and Symbols
    def test_numbers_and_symbols(self):
        self.assertEqual(levenshtein_distance("12345", "123456"), 1)  
        self.assertEqual(levenshtein_distance("100%", "100 percent"), 8) 
        self.assertEqual(levenshtein_distance("$100", "100 dollars"), 9)

    # Edge Cases
    def test_single_character_strings(self):
        self.assertEqual(levenshtein_distance("a", "b"), 1)  
        self.assertEqual(levenshtein_distance("a", "a"), 0) 
        self.assertEqual(levenshtein_distance("a", ""), 1) 

    def test_whitespace(self):
        self.assertEqual(levenshtein_distance("hello world", "helloworld"), 1) 
        self.assertEqual(levenshtein_distance("hello\tworld", "hello world"), 1)

    def test_repeated_characters(self):
        self.assertEqual(levenshtein_distance("aaaaa", "aaaab"), 1)  
        self.assertEqual(levenshtein_distance("aaaaa", "bbbbb"), 5)

if __name__ == "__main__":
    unittest.main()