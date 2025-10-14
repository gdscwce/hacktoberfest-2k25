from collections import Counter
from typing import List

def closeStrings(word1: str, word2: str) -> bool:
    # 1. Check if lengths are equal
    if len(word1) != len(word2):
        return False
    
    # Count character frequencies for both words
    count1 = Counter(word1)
    count2 = Counter(word2)
    
    # 2. Check if the set of unique characters is the same
    # We compare the keys (characters) of the Counter objects.
    # Note: Using .keys() on a Counter gives a view object which can be 
    # directly compared to another view object or a set.
    if count1.keys() != count2.keys():
        return False
    
    # 3. Check if the frequency distribution is the same
    # The list of frequencies (counts.values()) must be identical when sorted.
    # Sorting is necessary because Operation 2 means the character associated 
    # with a frequency can be different.
    return sorted(count1.values()) == sorted(count2.values())

# Example Usage:
word1_ex1 = "cabbba"
word2_ex1 = "abbccc"
# Unique Chars: {a, b, c} and {a, b, c} -> Match
# Frequencies: [1, 2, 3] and [1, 2, 3] -> Match
print(f"'{word1_ex1}' and '{word2_ex1}' are close: {closeStrings(word1_ex1, word2_ex1)}") # Output: True

word1_ex2 = "a"
word2_ex2 = "aa"
# Lengths are different (1 != 2)
print(f"'{word1_ex2}' and '{word2_ex2}' are close: {closeStrings(word1_ex2, word2_ex2)}") # Output: False

word1_ex3 = "aab"
word2_ex3 = "aac"
# Unique Chars: {a, b} and {a, c} -> Mismatch
print(f"'{word1_ex3}' and '{word2_ex3}' are close: {closeStrings(word1_ex3, word2_ex3)}") # Output: False
