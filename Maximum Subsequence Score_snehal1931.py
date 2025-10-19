import heapq
from typing import List

class Solution:
    """
    Pairs elements, sorts by nums2 in descending order. Uses a min-heap of size k 
    to maintain the k largest nums1 values for the current minimum nums2 value.
    """
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Create pairs and sort them by nums2 in descending order
        # We use a lambda to sort: -n2 is for descending order
        paired_values = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = [] # Min-heap to store the k largest nums1 values
        current_sum_n1 = 0
        max_score = 0
        
        for n1, n2 in paired_values:
            # Add current nums1 value to the heap and sum
            heapq.heappush(min_heap, n1)
            current_sum_n1 += n1
            
            # Maintain heap size at k
            if len(min_heap) > k:
                # Remove the smallest nums1 value to keep only the k largest
                smallest_n1 = heapq.heappop(min_heap)
                current_sum_n1 -= smallest_n1
            
            # If we have k elements, calculate the score
            if len(min_heap) == k:
                # Score is: (sum of k largest nums1 values) * (current nums2 value, which is the min)
                max_score = max(max_score, current_sum_n1 * n2)
                
        return max_score

# Example Usage:
# sol = Solution()
# sol.maxScore([1,3,3,2], [2,1,3,4], 3) # returns 12
