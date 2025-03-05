"""
Levenshtein Distance Implementation

This module provides an implementation of the Levenshtein distance algorithm,
which measures the minimum number of single-character edits (insertions, deletions,
or substitutions) required to change one string into another.

References:
- Levenshtein, V. I. (1966). "Binary codes capable of correcting deletions,
  insertions, and reversals". Soviet Physics Doklady, 10(8), 707-710.
- Wikipedia: Levenshtein distance. https://en.wikipedia.org/wiki/Levenshtein_distance
"""

def levenshtein_distance(str1, str2):
    """
    Compute the Levenshtein distance between two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The Levenshtein distance between str1 and str2.
    """
    if len(str1) < len(str2):
        return levenshtein_distance(str2, str1)

    if len(str2) == 0:
        return len(str1)

    previous_row = range(len(str2) + 1)
    for i, char1 in enumerate(str1):
        current_row = [i + 1]
        for j, char2 in enumerate(str2):
            substitution_cost = 0 if char1 == char2 else 1
            current_row.append(min(
                previous_row[j + 1] + 1,  # Deletion
                current_row[j] + 1,       # Insertion
                previous_row[j] + substitution_cost  # Substitution
            ))
        previous_row = current_row

    return previous_row[-1]