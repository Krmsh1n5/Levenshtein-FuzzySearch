"""
Performance Metrics for Fuzzy Search

This module provides functions to calculate accuracy, speed, and scalability of fuzzy search algorithms.

References:
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). "Introduction to Information Retrieval".
  Cambridge University Press.
"""

import time
from typing import List

def calculate_accuracy(query: str, targets: List[str], matches: List[str]) -> float:
    """
    Calculate the accuracy of the fuzzy search results.

    Args:
        query (str): The search query.
        targets (List[str]): List of target strings.
        matches (List[str]): List of matched strings.

    Returns:
        float: The accuracy of the search results (between 0 and 1).
    """
    # Assume the first target is the correct match for simplicity
    correct_match = targets[0]
    if correct_match in matches:
        return 1.0
    return 0.0


def measure_speed(search_func, query: str, targets: List[str], *args, **kwargs) -> float:
    """
    Measure the time taken to perform a fuzzy search.

    Args:
        search_func (callable): The fuzzy search function to benchmark.
        query (str): The search query.
        targets (List[str]): List of target strings.
        *args, **kwargs: Additional arguments for the search function.

    Returns:
        float: The time taken in seconds.
    """
    start_time = time.time()
    search_func(query, targets, *args, **kwargs)
    end_time = time.time()
    return end_time - start_time


def measure_scalability(search_func, query: str, targets: List[str], dataset_sizes: List[int]) -> List[float]:
    """
    Measure the scalability of the fuzzy search algorithm by testing it on datasets of different sizes.

    Args:
        search_func (callable): The fuzzy search function to benchmark.
        query (str): The search query.
        targets (List[str]): List of target strings.
        dataset_sizes (List[int]): List of dataset sizes to test.

    Returns:
        List[float]: The time taken for each dataset size.
    """
    times = []
    for size in dataset_sizes:
        subset = targets[:size]
        time_taken = measure_speed(search_func, query, subset)
        times.append(time_taken)
    return times