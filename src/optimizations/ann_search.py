"""
Approximate Nearest Neighbor (ANN) Search using FAISS

This module provides an implementation of ANN search using the FAISS library, which is
optimized for fast similarity search in high-dimensional spaces.

References:
- Johnson, J., Douze, M., & Jégou, H. (2019). "Billion-scale similarity search with GPUs".
  IEEE Transactions on Big Data, 7(3), 535-547.
- FAISS Documentation. https://faiss.ai/
"""

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def build_faiss_index(targets):
    """
    Build a FAISS index for the given target strings.

    Args:
        targets (list): List of target strings.

    Returns:
        faiss.IndexFlatL2: A FAISS index.
        np.ndarray: Embeddings of the target strings.
    """
    embeddings = model.encode(targets)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, embeddings

def ann_search(query, index, targets, k=5):
    """
    Perform approximate nearest neighbor search using FAISS.

    Args:
        query (str): The search query.
        index (faiss.IndexFlatL2): The FAISS index.
        targets (list): List of target strings.
        k (int): The number of nearest neighbors to return.

    Returns:
        list: List of tuples (matched string, distance).
    """
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    results = []
    for i, distance in zip(indices[0], distances[0]):
        if i != -1:  # FAISS returns -1 for invalid indices
            results.append((targets[i], distance))
    return results