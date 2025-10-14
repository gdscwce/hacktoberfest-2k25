from typing import List
from collections import Counter

def uniqueOccurrences(arr: List[int]) -> bool:
    """
    Checks if the number of occurrences of each value in the array is unique.

    Args:
        arr: The input array of integers.

    Returns:
        True if all occurrence counts are unique, False otherwise.
    """
    
    # Step 1: Count the frequency of each element in the array.
    # 'counts' will be a dictionary-like object: {number: frequency}
    counts = Counter(arr)
    
    # Step 2: Extract all the frequency values.
    all_frequencies = counts.values()
    
    # Step 3: Check for uniqueness.
    # If the length of the set of frequencies is equal to the length of 
    # the list of frequencies, it means there were no duplicate frequencies.
    # len(set(all_frequencies)) removes duplicates and gives unique counts.
    # len(all_frequencies) gives the total number of distinct elements (keys).
    return len(set(all_frequencies)) == len(all_frequencies)

# Example Usage:
arr1 = [1, 2, 2, 1, 1, 3]
# Frequencies: 1 (3 times), 2 (2 times), 3 (1 time). Counts: [3, 2, 1]. All unique.
print(f"[{arr1}] -> {uniqueOccurrences(arr1)}")  # Output: True

arr2 = [1, 2]
# Frequencies: 1 (1 time), 2 (1 time). Counts: [1, 1]. Not unique.
print(f"[{arr2}] -> {uniqueOccurrences(arr2)}")  # Output: False

arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# Frequencies: -3 (3 times), 0 (2 times), 1 (4 times), 10 (1 time). Counts: [3, 2, 4, 1]. All unique.
print(f"[{arr3}] -> {uniqueOccurrences(arr3)}")  # Output: True
