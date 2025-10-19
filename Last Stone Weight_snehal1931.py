import heapq
from typing import List

class Solution:
    """
    Uses a max-heap (implemented by negating values in a min-heap) 
    to efficiently get the two heaviest stones.
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a Max Heap by negating all weights
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Extract the two heaviest stones (most negative values)
            y = -heapq.heappop(max_heap) # Heaviest
            x = -heapq.heappop(max_heap) # Second Heaviest
            
            if x != y:
                # If weights are different, push the remaining difference back
                # Since y >= x, y - x >= 0. We push -(y - x) to maintain max-heap
                heapq.heappush(max_heap, -(y - x))
                
        # If the heap is empty, return 0. Otherwise, return the last stone's weight.
        return -max_heap[0] if max_heap else 0

# Example Usage:
# sol = Solution()
# sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) # returns 1
