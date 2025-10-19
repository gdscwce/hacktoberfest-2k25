from typing import List

class TrieNode:
    # ... (same as above for Trie)
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.words = [] # Stores products that pass through this node

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 1. Build the Trie
        root = TrieNode()
        products.sort() # Sort for lexicographical order of suggestions

        for product in products:
            curr = root
            for char in product:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # Store up to 3 products lexicographically
                if len(curr.words) < 3:
                    curr.words.append(product)

        # 2. Search and collect suggestions
        res = []
        curr = root
        
        for i, char in enumerate(searchWord):
            if curr and char in curr.children:
                curr = curr.children[char]
                res.append(curr.words)
            else:
                # No more matches, all subsequent suggestions will be empty
                res.append([])
                curr = None # Stop further search

        return res
