"""
Weighted Edit Distance Implementation

This module provides an implementation of the weighted edit distance algorithm,
which assigns different costs to insertions, deletions, substitutions, and transpositions.

References:
- Wagner, R. A., & Fischer, M. J. (1974). "The string-to-string correction problem".
  Journal of the ACM, 21(1), 168-173.
"""

def weighted_edit_distance(str1, str2, weights):
    """
    Compute the weighted edit distance between two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.
        weights (tuple): A tuple of weights for (insertion, deletion, substitution, transposition).

    Returns:
        int: The weighted edit distance between str1 and str2.
    """
    insert_cost, delete_cost, substitute_cost, transpose_cost = weights

    if len(str1) < len(str2):
        return weighted_edit_distance(str2, str1, weights)

    if len(str2) == 0:
        return len(str1) * delete_cost

    d = {}
    len1, len2 = len(str1), len(str2)
    for i in range(-1, len1 + 1):
        d[(i, -1)] = (i + 1) * delete_cost
    for j in range(-1, len2 + 1):
        d[(-1, j)] = (j + 1) * insert_cost

    for i in range(len1):
        for j in range(len2):
            substitution_cost = 0 if str1[i] == str2[j] else substitute_cost
            d[(i, j)] = min(
                d[(i - 1, j)] + delete_cost,  # Deletion
                d[(i, j - 1)] + insert_cost,  # Insertion
                d[(i - 1, j - 1)] + substitution_cost  # Substitution
            )
            if i > 0 and j > 0 and str1[i] == str2[j - 1] and str1[i - 1] == str2[j]:
                d[(i, j)] = min(
                    d[(i, j)],
                    d[(i - 2, j - 2)] + transpose_cost  # Transposition
                )

    return d[(len1 - 1, len2 - 1)]