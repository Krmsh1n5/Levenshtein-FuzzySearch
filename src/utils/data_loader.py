"""
Data Loader Utility

This module provides functions to load datasets from various file formats (e.g., CSV).

References:
- Pandas Documentation. https://pandas.pydata.org/docs/
"""

import pandas as pd
from typing import List

def load_csv(file_path: str, column_name: str) -> List[str]:
    """
    Load a dataset from a CSV file and extract a specific column as a list of strings.

    Args:
        file_path (str): The path to the CSV file.
        column_name (str): The name of the column to extract.

    Returns:
        List[str]: A list of strings from the specified column.
    """
    try:
        df = pd.read_csv(file_path)
        return df[column_name].tolist()
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return []


def load_txt(file_path: str) -> List[str]:
    """
    Load a dataset from a text file where each line is a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        List[str]: A list of strings from the text file.
    """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error loading text file: {e}")
        return []