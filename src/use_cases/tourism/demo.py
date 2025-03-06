"""
Demo of tourism location search using real-world queries
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/use_cases/tourism')))

from search import TourismSearchEngine

def load_locations():
    return [
        "La Habana", "Punta Blanca", 
        "Saint George's Anglican Church",
        "Autopista a Pinar del Río"
    ]

def main():
    engine = TourismSearchEngine(load_locations())
    
    # Test queries with expected matches
    test_queries = [
        ("Punta Blanka", "Punta Blanca"),
        ("Saint Gorge", "Saint George's Anglican Church"),
        ("La Havana", "La Habana")
    ]
    
    print("Tourism Location Search Results:")
    for query, expected in test_queries:
        print(f"\nQuery: '{query}'")
        results = engine.search(query)
        print(f"Expected: {expected}")
        print("Matches:")
        for loc, score in results:
            print(f"- {loc} ({score:.1%})")

if __name__ == "__main__":
    main()