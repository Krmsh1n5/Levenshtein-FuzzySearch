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
from functools import partial
from itertools import islice
from rapidfuzz.distance import Levenshtein  # Faster than python-Levenshtein

def chunker(iterable, chunk_size):
    """Memory-efficient chunking for large datasets"""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, chunk_size)):
        yield chunk

def search_worker(query, threshold, target):
    """Optimized search worker with pre-bound parameters"""
    distance = Levenshtein.distance(query, target)
    return (target, distance) if distance <= threshold else None

def parallel_fuzzy_search(query, targets, max_distance=2, min_parallel_size=5000, n_jobs=None):
    """
    Hybrid parallel/linear search with automatic mode switching
    
    Args:
        query: Search string
        targets: List of target strings
        max_distance: Maximum allowed Levenshtein distance
        min_parallel_size: Minimum dataset size to trigger parallel mode
        n_jobs: Number of parallel workers (None = auto-detect)
    """
    # Fallback to linear search for small datasets
    if len(targets) < min_parallel_size:
        return sorted(
            ((t, Levenshtein.distance(query, t)) for t in targets if Levenshtein.distance(query, t) <= max_distance),
            key=lambda x: (x[1], x[0])
        )

    # Configure parallel execution
    n_jobs = n_jobs or cpu_count()
    worker = partial(search_worker, query, max_distance)
    
    # Optimized chunk size calculation
    chunk_size = max(1000, len(targets) // (n_jobs * 4))
    
    with Pool(n_jobs) as pool:
        results = []
        # Process in chunks to balance load and memory usage
        for chunk in chunker(targets, chunk_size):
            chunk_results = pool.map(worker, chunk)
            results.extend(r for r in chunk_results if r is not None)

    # Final sorting and deduplication
    return sorted(results, key=lambda x: (x[1], x[0]))