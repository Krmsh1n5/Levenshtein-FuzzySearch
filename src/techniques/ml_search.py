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
import jellyfish

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-mpnet-base-v2')  # More robust model

def preprocess(text):
    """
    Preprocess the input text by lowercasing and removing special characters.
    """
    return text.lower().strip()

def semantic_similarity(str1, str2):
    """
    Compute the semantic similarity between two strings using sentence embeddings.
    """
    # Preprocess the input strings
    str1 = preprocess(str1)
    str2 = preprocess(str2)

    embeddings = model.encode([str1, str2])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

def ml_fuzzy_search(query, targets, threshold=0.4):  # Lowered threshold
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

def hybrid_fuzzy_search(query, targets, ml_threshold=0.4, edit_threshold=2):
    """
    Perform fuzzy search using a hybrid approach (ML-based + edit distance).
    """
    matches = []
    for target in targets:
        # Compute ML-based similarity
        ml_similarity = semantic_similarity(query, target)
        
        # Compute edit distance
        edit_distance = jellyfish.levenshtein_distance(query, target)
        
        # Match if either condition is met
        if ml_similarity >= ml_threshold or edit_distance <= edit_threshold:
            matches.append((target, ml_similarity, edit_distance))
    
    # Sort by ML similarity (higher is better) and edit distance (lower is better)
    matches.sort(key=lambda x: (-x[1], x[2]))
    return [match[0] for match in matches]