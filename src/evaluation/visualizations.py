"""
Visualizations for Performance Analysis

This module provides functions to generate graphs and charts for analyzing the performance
of fuzzy search algorithms.

References:
- Matplotlib Documentation. https://matplotlib.org/stable/contents.html
"""

import matplotlib.pyplot as plt
from typing import List

def plot_query_time_vs_dataset_size(dataset_sizes: List[int], times: List[float], title: str):
    """
    Plot the query time vs. dataset size.

    Args:
        dataset_sizes (List[int]): List of dataset sizes.
        times (List[float]): List of query times.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dataset_sizes, times, marker='o')
    plt.xlabel("Dataset Size")
    plt.ylabel("Query Time (seconds)")
    plt.title(title)
    plt.grid(True)
    plt.savefig("results/visualizations/query_time_vs_dataset_size.png")
    plt.close()


def plot_accuracy_vs_threshold(thresholds: List[int], accuracies: List[float], title: str):
    """
    Plot the accuracy vs. edit distance threshold.

    Args:
        thresholds (List[int]): List of edit distance thresholds.
        accuracies (List[float]): List of accuracies.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(thresholds, accuracies, marker='o')
    plt.xlabel("Edit Distance Threshold")
    plt.ylabel("Accuracy")
    plt.title(title)
    plt.grid(True)
    plt.savefig("results/visualizations/accuracy_vs_threshold.png")
    plt.close()