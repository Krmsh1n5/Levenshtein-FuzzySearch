"""
Miscellaneous Helper Functions

This module provides miscellaneous helper functions for the fuzzy search system.
"""

from typing import List, Tuple

def split_name(full_name: str) -> Tuple[str, str]:
    """
    Split a full name into first name and last name.

    Args:
        full_name (str): The full name to split.

    Returns:
        Tuple[str, str]: A tuple containing the first name and last name.
    """
    parts = full_name.split()
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], " ".join(parts[1:])


def chunk_list(lst: List, chunk_size: int) -> List[List]:
    """
    Split a list into smaller chunks of a specified size.

    Args:
        lst (List): The list to split.
        chunk_size (int): The size of each chunk.

    Returns:
        List[List]: A list of smaller chunks.
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def flatten_list(nested_list: List[List]) -> List:
    """
    Flatten a nested list into a single list.

    Args:
        nested_list (List[List]): The nested list to flatten.

    Returns:
        List: The flattened list.
    """
    return [item for sublist in nested_list for item in sublist]