"""
Machine Learning-Based Fuzzy Search

This module provides an implementation of machine learning-based fuzzy search using
sentence embeddings (e.g., Word2Vec, BERT) to compute semantic similarity.

References:
- Reimers, N., & Gurevych, I. (2019). "Sentence-BERT: Sentence Embeddings using
  Siamese BERT-Networks". Proceedings of EMNLP-IJCNLP, 3980-3990.
- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of
  Word Representations in Vector Space". arXiv preprint arXiv:1301.3781.
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(str1, str2):
    """
    Compute the semantic similarity between two strings using sentence embeddings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        float: The cosine similarity score between -1 and 1.
    """
    embeddings = model.encode([str1, str2])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]


def ml_fuzzy_search(query, targets, threshold=0.7):
    """
    Perform fuzzy search using machine learning-based semantic similarity.

    Args:
        query (str): The search query.
        targets (list): List of target strings to search in.
        threshold (float): The minimum similarity score for a match.

    Returns:
        list: List of tuples (matched string, similarity score).
    """
    matches = []
    for target in targets:
        similarity = semantic_similarity(query, target)
        if similarity >= threshold:
            matches.append((target, similarity))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches