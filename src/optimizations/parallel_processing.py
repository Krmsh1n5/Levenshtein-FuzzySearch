"""
Parallel Processing for Large-Scale Fuzzy Search

This module provides an implementation of parallel processing for fuzzy search using
the `joblib` library, which is useful for speeding up computations on large datasets.

References:
- Pedregosa, F., et al. (2011). "Scikit-learn: Machine Learning in Python".
  Journal of Machine Learning Research, 12, 2825-2830.
- Joblib Documentation. https://joblib.readthedocs.io/
"""

from joblib import Parallel, delayed
from Levenshtein import distance as levenshtein_distance

def parallel_fuzzy_search(query, targets, threshold=3, n_jobs=-1):
    """
    Perform fuzzy search in parallel using multiple CPU cores.

    Args:
        query (str): The search query.
        targets (list): List of target strings to search in.
        threshold (int): The maximum allowed Levenshtein distance.
        n_jobs (int): The number of CPU cores to use (-1 for all available cores).

    Returns:
        list: List of tuples (matched string, distance).
    """
    def search_target(query, target, threshold):
        distance = levenshtein_distance(query, target)
        if distance <= threshold:
            return (target, distance)
        return None

    results = Parallel(n_jobs=n_jobs)(delayed(search_target)(query, target, threshold) for target in targets)
    return [result for result in results if result is not None]