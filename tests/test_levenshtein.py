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
        self.assertEqual(levenshtein_distance("kitten", "sitten"), 1)  # Substitution
        self.assertEqual(levenshtein_distance("kitten", "kittens"), 1)  # Insertion
        self.assertEqual(levenshtein_distance("kitten", "itten"), 1)  # Deletion

    def test_multiple_edits(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)  # Substitution + Insertion

    def test_empty_string(self):
        self.assertEqual(levenshtein_distance("", "kitten"), 6)  # All insertions
        self.assertEqual(levenshtein_distance("kitten", ""), 6)  # All deletions

    # Case Sensitivity
    def test_case_sensitivity(self):
        self.assertEqual(levenshtein_distance("Kitten", "kitten"), 1)  # Case difference
        self.assertEqual(levenshtein_distance("HELLO", "hello"), 5)  # All characters differ in case

    # Unicode and Special Characters
    def test_unicode_characters(self):
        self.assertEqual(levenshtein_distance("café", "cafe"), 1)  # Unicode character substitution
        self.assertEqual(levenshtein_distance("こんにちは", "こんにちわ"), 1)  # Japanese characters
        self.assertEqual(levenshtein_distance("straße", "strasse"), 2)  # German characters

    def test_special_characters(self):
        self.assertEqual(levenshtein_distance("hello!", "hello?"), 1)  # Special character substitution
        self.assertEqual(levenshtein_distance("hello#world", "hello@world"), 1)  # Special character substitution

    # Real-World Scenarios
    def test_real_world_names(self):
        self.assertEqual(levenshtein_distance("Christopher", "Kristofer"), 4)  # Common name variation
        self.assertEqual(levenshtein_distance("Jennifer", "Jenifer"), 1)  # Common typo

    def test_real_world_addresses(self):
        self.assertEqual(levenshtein_distance("123 Main St", "123 Main Street"), 4)  # Abbreviation
        self.assertEqual(levenshtein_distance("Apt 4B", "Apartment 4B"), 6)  # Abbreviation

    def test_real_world_typos(self):
        self.assertEqual(levenshtein_distance("accomodation", "accommodation"), 1)  # Common typo
        self.assertEqual(levenshtein_distance("recieve", "receive"), 2)  # Common typo

    # Long Strings
    def test_long_strings(self):
        str1 = "a" * 1000
        str2 = "b" * 1000
        self.assertEqual(levenshtein_distance(str1, str2), 1000)  # All characters differ

    # Mixed Cases
    def test_mixed_case_strings(self):
        self.assertEqual(levenshtein_distance("HelloWorld", "helloworld"), 2)  # Mixed case
        self.assertEqual(levenshtein_distance("PythonCode", "pythoncode"), 2)  # Mixed case

    # Numbers and Symbols
    def test_numbers_and_symbols(self):
        self.assertEqual(levenshtein_distance("12345", "123456"), 1)  # Number insertion
        self.assertEqual(levenshtein_distance("100%", "100 percent"), 8)  # Symbol vs. word
        self.assertEqual(levenshtein_distance("$100", "100 dollars"), 9)  # Symbol vs. word

    # Edge Cases
    def test_single_character_strings(self):
        self.assertEqual(levenshtein_distance("a", "b"), 1)  # Single character substitution
        self.assertEqual(levenshtein_distance("a", "a"), 0)  # Single character identical
        self.assertEqual(levenshtein_distance("a", ""), 1)  # Single character deletion

    def test_whitespace(self):
        self.assertEqual(levenshtein_distance("hello world", "helloworld"), 1)  # Space insertion
        self.assertEqual(levenshtein_distance("hello\tworld", "hello world"), 1)  # Tab vs. space

    def test_repeated_characters(self):
        self.assertEqual(levenshtein_distance("aaaaa", "aaaab"), 1)  # Repeated characters
        self.assertEqual(levenshtein_distance("aaaaa", "bbbbb"), 5)  # All characters differ

if __name__ == "__main__":
    unittest.main()