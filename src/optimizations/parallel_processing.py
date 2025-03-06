"""
Parallel Processing for Large-Scale Fuzzy Search

This module provides an implementation of parallel processing for fuzzy search using
the `joblib` library, which is useful for speeding up computations on large datasets.

References:
- Pedregosa, F., et al. (2011). "Scikit-learn: Machine Learning in Python".
  Journal of Machine Learning Research, 12, 2825-2830.
- Joblib Documentation. https://joblib.readthedocs.io/
"""

from multiprocessing import Pool, cpu_count
from Levenshtein import distance as levenshtein_distance

def search_target(query, target, threshold):
    """
    Helper function to compute the Levenshtein distance and check if it's within the threshold.

    Args:
        query (str): The search query.
        target (str): The target string.
        threshold (int): The maximum allowed Levenshtein distance.

    Returns:
        tuple: (target, distance) if the distance is within the threshold, otherwise None.
    """
    distance = levenshtein_distance(query, target)
    if distance <= threshold:
        return (target, distance)
    return None

def process_chunk(query, chunk, threshold):
    """
    Process a chunk of targets in parallel.

    Args:
        query (str): The search query.
        chunk (list): A chunk of target strings.
        threshold (int): The maximum allowed Levenshtein distance.

    Returns:
        list: List of tuples (matched string, distance).
    """
    return [search_target(query, target, threshold) for target in chunk]

def parallel_fuzzy_search(query, targets, threshold=3, n_jobs=None):
    """
    Perform fuzzy search in parallel using multiple CPU cores.

    Args:
        query (str): The search query.
        targets (list): List of target strings to search in.
        threshold (int): The maximum allowed Levenshtein distance.
        n_jobs (int): The number of CPU cores to use (default: all available cores).

    Returns:
        list: List of tuples (matched string, distance).
    """
    # Use all available cores if n_jobs is None
    if n_jobs is None:
        n_jobs = cpu_count()

    # Split targets into chunks to reduce overhead
    chunk_size = max(1, len(targets) // (n_jobs * 4))  # Adjust chunk size based on number of jobs
    chunks = [targets[i:i + chunk_size] for i in range(0, len(targets), chunk_size)]

    # Use multiprocessing.Pool for parallel processing
    with Pool(processes=n_jobs) as pool:
        results = pool.starmap(
            process_chunk,
            [(query, chunk, threshold) for chunk in chunks]
        )

    # Flatten the results and filter out None values
    matches = [result for chunk_results in results for result in chunk_results if result is not None]
    return matches