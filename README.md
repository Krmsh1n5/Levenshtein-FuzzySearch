# Levenshtein-FuzzySearch

This repository is a comprehensive research platform dedicated to exploring the Levenshtein distance and its various applications in fuzzy matching and search. It includes a wide range of implementations, optimizations, and techniques designed to handle real-world data challenges.

## Repository Structure

- **data/**  
  Contains real-world datasets used for experimentation. In particular, it includes a sample dataset obtained from [Geofabrik Central America](https://download.geofabrik.de/central-america.html). This dataset serves as the basis for applying and testing the Levenshtein-based techniques on practical data.

- **notebooks/**  
  Hosts a Jupyter Notebook that demonstrates a simple application of the Levenshtein distance on the real-world data. This notebook provides a walkthrough for preprocessing, computing distances, and evaluating fuzzy search outcomes on noisy and heterogeneous data.

- **src/**  
  This is the core of the repository and is divided into several submodules:
  
  - **algorithms/**  
    Implements multiple variants of the edit distance:
    - **Bit Parallel Method:** An efficient bit-level implementation for faster computations.
    - **Damerau-Levenshtein Distance:** An extension that also accounts for transpositions.
    - **Classic Levenshtein Distance:** The standard dynamic programming approach.
    - **Weighted Edit Distance:** Allows for custom weighting of operations to suit specific application needs.
  
  - **optimizations/**  
    Contains advanced search implementations and performance enhancements:
    - **ANN (Approximate Nearest Neighbor) Search:** For scalable similarity searches.
    - **BK Tree:** A specialized tree structure for efficient search in metric spaces.
    - **Parallel Processing:** Techniques for concurrent processing of large datasets.
  
  - **techniques/**  
    Explores alternative fuzzy search methods:
    - **ML Search:** Machine learning-based approaches to refine search results.
    - **N-Gram Search:** Breaking strings into n-grams to improve matching performance.
    - **Phonetic Search:** Techniques such as Soundex or Metaphone to match words based on sound similarity.

- **tests/**  
  Contains unit tests covering:
  - Basic algorithm functions.
  - Fuzzy search implementations.
  - Optimization routines.
  
  These tests ensure the reliability and correctness of the implementations across the algorithms and techniques.

## Real-World Application

The repository is designed to bridge theoretical research with practical applications. By leveraging the real-world data from Geofabrik, the platform demonstrates:
- **Robust Matching:** How different edit distance algorithms and fuzzy matching techniques can be applied to imperfect data.
- **Performance Optimization:** A detailed look into how BK Trees, and parallel processing can significantly reduce the computational cost, especially when dealing with large datasets.
