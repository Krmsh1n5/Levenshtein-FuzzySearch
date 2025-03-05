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

def phonetic_similarity(str1, str2):
    """
    Compute the phonetic similarity between two strings using Soundex and Metaphone.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the strings are phonetically similar, False otherwise.
    """
    soundex_match = soundex(str1) == soundex(str2)

    # Compare Metaphone codes (both primary and secondary)
    metaphone_codes1 = metaphone(str1)
    metaphone_codes2 = metaphone(str2)
    metaphone_match = (
        metaphone_codes1[0] == metaphone_codes2[0] or  # Primary codes match
        metaphone_codes1[0] == metaphone_codes2[1] or  # Primary matches secondary
        metaphone_codes1[1] == metaphone_codes2[0] or  # Secondary matches primary
        metaphone_codes1[1] == metaphone_codes2[1]     # Secondary codes match
    )

    # Return True if either Soundex or Metaphone codes match
    return soundex_match or metaphone_match


def phonetic_fuzzy_search(query, targets):
    """
    Perform fuzzy search using phonetic algorithms.

    Args:
        query (str): The search query.
        targets (list): List of target strings to search in.

    Returns:
        list: List of matched strings.
    """
    matches = []
    for target in targets:
        if phonetic_similarity(query, target):
            matches.append(target)
    return matches