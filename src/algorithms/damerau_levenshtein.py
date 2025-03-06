"""
Damerau-Levenshtein Distance Implementation

This module provides an implementation of the Damerau-Levenshtein distance algorithm,
which extends the Levenshtein distance by including transpositions (swaps of adjacent characters).

References:
- Damerau, F. J. (1964). "A technique for computer detection and correction of spelling errors".
  Communications of the ACM, 7(3), 171-176.
- Wikipedia: Damerau-Levenshtein distance. https://en.wikipedia.org/wiki/Damerau-Levenshtein_distance
"""

def damerau_levenshtein_distance(str1, str2):
    """
    Compute the Damerau-Levenshtein distance between two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The Damerau-Levenshtein distance between str1 and str2.
    """
    if len(str1) < len(str2):
        return damerau_levenshtein_distance(str2, str1)

    if len(str2) == 0:
        return len(str1)

    d = {}
    len1, len2 = len(str1), len(str2)
    for i in range(-1, len1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len2 + 1):
        d[(-1, j)] = j + 1

    for i in range(len1):
        for j in range(len2):
            substitution_cost = 0 if str1[i] == str2[j] else 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # Deletion
                d[(i, j - 1)] + 1,  # Insertion
                d[(i - 1, j - 1)] + substitution_cost  # Substitution
            )
            if i > 0 and j > 0 and str1[i] == str2[j - 1] and str1[i - 1] == str2[j]:
                d[(i, j)] = min(
                    d[(i, j)],
                    d[(i - 2, j - 2)] + substitution_cost  # Transposition
                )

    return d[(len1 - 1, len2 - 1)]