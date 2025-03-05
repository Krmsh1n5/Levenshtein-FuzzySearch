"""
String Preprocessing Utility

This module provides functions to preprocess strings (e.g., lowercase, remove punctuation).

References:
- Natural Language Toolkit (NLTK) Documentation. https://www.nltk.org/
"""

import string
from typing import List

def lowercase(text: str) -> str:
    """
    Convert a string to lowercase.

    Args:
        text (str): The input string.

    Returns:
        str: The lowercase version of the string.
    """
    return text.lower()


def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from a string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with punctuation removed.
    """
    return text.translate(str.maketrans('', '', string.punctuation))


def preprocess_string(text: str) -> str:
    """
    Preprocess a string by converting it to lowercase and removing punctuation.

    Args:
        text (str): The input string.

    Returns:
        str: The preprocessed string.
    """
    text = lowercase(text)
    text = remove_punctuation(text)
    return text


def preprocess_list(strings: List[str]) -> List[str]:
    """
    Preprocess a list of strings.

    Args:
        strings (List[str]): The list of strings to preprocess.

    Returns:
        List[str]: The list of preprocessed strings.
    """
    return [preprocess_string(s) for s in strings]