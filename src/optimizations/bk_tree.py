"""
BK-Tree Implementation for Efficient Fuzzy Search

This module provides an implementation of a BK-tree (Burkhard-Keller tree), a data structure
for efficient search of strings within a given edit distance.

References:
- Burkhard, W. A., & Keller, R. M. (1973). "Some approaches to best-match file searching".
  Communications of the ACM, 16(4), 230-236.
- Wikipedia: BK-tree. https://en.wikipedia.org/wiki/BK-tree
"""
class BKTree:
    def __init__(self, words, distance_func):
        """
        Initialize the BK-tree with a list of words and a distance function.
        
        Args:
            words (list): A list of words to insert into the tree.
            distance_func (callable): A function that computes the distance between two strings.
        """
        self.root = None
        self.distance_func = distance_func
        for word in words:
            self.insert(word)

    def insert(self, word):
        """
        Insert a word into the BK-tree.
        
        Args:
            word (str): The word to insert.
        """
        if self.root is None:
            self.root = (word, {})
            return

        current_node = self.root
        while True:
            current_word, children = current_node
            distance = self.distance_func(current_word, word)
            if distance == 0:
                return  # Word already exists in the tree
            if distance in children:
                current_node = children[distance]
            else:
                children[distance] = (word, {})
                break

    def search(self, query, max_distance):
        """
        Search for words within a given maximum distance from the query.
        
        Args:
            query (str): The query string.
            max_distance (int): The maximum allowed distance.

        Returns:
            list: List of tuples (word, distance) within the maximum distance.
        """
        if self.root is None:
            return []

        results = []
        stack = [self.root]
        while stack:
            current_word, children = stack.pop()
            distance = self.distance_func(current_word, query)
            if distance <= max_distance:
                results.append((current_word, distance))
            # Search only existing children
            for d, child in children.items():
                if abs(d - distance) <= max_distance:
                    stack.append(child)
        return sorted(results, key=lambda x: x[1])  # Sort by closest match
