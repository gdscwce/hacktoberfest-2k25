import heapq
from typing import List

class Solution:
    """
    Uses a Max Heap of size k to store the k points with the smallest distance.
    The largest distance in the heap is popped if a new closer point is found.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max-heap to store tuples: (negative_squared_distance, x, y)
        # Storing negative distance simulates a Max Heap on distance.
        max_heap = []
        
        for x, y in points:
            # Squared distance: x^2 + y^2
            dist_sq = x * x + y * y
            
            # Push (-distance_sq, x, y) onto the max heap
            heapq.heappush(max_heap, (-dist_sq, x, y))
            
            # If heap size exceeds k, pop the element with the largest distance (most negative -distance_sq)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract the k points from the heap
        # The points are in (x, y) format at indices 1 and 2 of the tuple
        return [[x, y] for (dist, x, y) in max_heap]

# Example Usage:
# sol = Solution()
# sol.kClosest([[1,3], [-2,2]], 1) # returns [[-2, 2]]
