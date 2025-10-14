from typing import List, Set

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """
    Finds the distinct elements in each array that are not present in the other.
    
    Args:
        nums1: The first integer array.
        nums2: The second integer array.
        
    Returns:
        A list of two lists:
        - The first list contains elements unique to nums1.
        - The second list contains elements unique to nums2.
    """
    
    # Convert lists to sets to automatically handle duplicates and enable 
    # O(1) average time complexity for the difference operation.
    set1: Set[int] = set(nums1)
    set2: Set[int] = set(nums2)
    
    # Calculate the set difference:
    # 1. set1 - set2: elements in set1 but not in set2
    # 2. set2 - set1: elements in set2 but not in set1
    
    diff1_list = list(set1 - set2)
    diff2_list = list(set2 - set1)
    
    return [diff1_list, diff2_list]

# Example Usage:
nums1_ex1 = [1, 2, 3]
nums2_ex1 = [2, 4, 6]
# Output: [[1, 3], [4, 6]]
print(f"Difference for Ex1: {findDifference(nums1_ex1, nums2_ex1)}") 

nums1_ex2 = [1, 2, 3, 3]
nums2_ex2 = [1, 1, 2, 2]
# Output: [[3], []]
print(f"Difference for Ex2: {findDifference(nums1_ex2, nums2_ex2)}")
