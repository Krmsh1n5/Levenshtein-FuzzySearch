"""
Benchmarking Fuzzy Search Implementations

This module provides functions to compare the performance of your fuzzy search implementation
with existing tools like FuzzyWuzzy and Elasticsearch.

References:
- Cohen, W. W., Ravikumar, P., & Fienberg, S. E. (2003). "A comparison of string distance metrics
  for name-matching tasks". Proceedings of the IJCAI-03 Workshop on Information Integration.
- Elasticsearch Documentation. https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
"""

from fuzzywuzzy import fuzz
from performance_metrics import measure_speed
from typing import List, Tuple


def benchmark_fuzzywuzzy(query: str, targets: List[str]) -> List[Tuple[str, int]]:
    """
    Perform fuzzy search using FuzzyWuzzy and return matches with their similarity scores.

    Args:
        query (str): The search query.
        targets (List[str]): List of target strings.

    Returns:
        List[Tuple[str, int]]: List of tuples (matched string, similarity score).
    """
    matches = []
    for target in targets:
        score = fuzz.ratio(query, target)
        matches.append((target, score))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches


def benchmark_elasticsearch(query: str, targets: List[str]) -> List[Tuple[str, float]]:
    """
    Perform fuzzy search using Elasticsearch (requires an Elasticsearch instance to be running).

    Args:
        query (str): The search query.
        targets (List[str]): List of target strings.

    Returns:
        List[Tuple[str, float]]: List of tuples (matched string, relevance score).
    """
    # Placeholder for Elasticsearch implementation
    # You need to set up an Elasticsearch instance and index the targets first.
    # This is just a mock implementation.
    matches = []
    for target in targets:
        if query.lower() in target.lower():
            matches.append((target, 1.0))
    return matches


def compare_implementations(query: str, targets: List[str], search_func):
    """
    Compare the performance of your fuzzy search implementation with FuzzyWuzzy and Elasticsearch.

    Args:
        query (str): The search query.
        targets (List[str]): List of target strings.
        search_func (callable): Your fuzzy search function.

    Returns:
        dict: A dictionary containing the time taken by each implementation.
    """
    results = {}

    # Benchmark your implementation
    results["your_implementation"] = measure_speed(search_func, query, targets)

    # Benchmark FuzzyWuzzy
    results["fuzzywuzzy"] = measure_speed(benchmark_fuzzywuzzy, query, targets)

    # Benchmark Elasticsearch
    results["elasticsearch"] = measure_speed(benchmark_elasticsearch, query, targets)

    return results