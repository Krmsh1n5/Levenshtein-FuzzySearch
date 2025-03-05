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

from nltk.util import ngrams

def ngram_similarity(str1, str2, n=2):
    """
    Compute the similarity between two strings using n-grams.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.
        n (int): The length of the n-grams.

    Returns:
        float: The similarity score between 0 and 1.
    """
    ngrams1 = set(ngrams(str1, n))
    ngrams2 = set(ngrams(str2, n))
    intersection = ngrams1.intersection(ngrams2)
    union = ngrams1.union(ngrams2)
    return len(intersection) / len(union) if union else 0.0


def ngram_fuzzy_search(query, targets, n=2, threshold=0.5):
    """
    Perform fuzzy search using n-gram similarity.

    Args:
        query (str): The search query.
        targets (list): List of target strings to search in.
        n (int): The length of the n-grams.
        threshold (float): The minimum similarity score for a match.

    Returns:
        list: List of tuples (matched string, similarity score).
    """
    matches = []
    for target in targets:
        similarity = ngram_similarity(query, target, n)
        if similarity >= threshold:
            matches.append((target, similarity))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches