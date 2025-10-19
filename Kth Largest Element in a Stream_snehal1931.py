import heapq
from typing import List

class KthLargest:
    """
    Uses a min-heap of size k to store the k largest elements. 
    The root (smallest element in the heap) is the kth largest element overall.
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Initialize a min-heap
        self.min_heap = []
        
        # Add initial numbers to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap size exceeds k, remove the smallest element (root)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap is the kth largest element
        return self.min_heap[0]

# Example Usage:
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# kthLargest.add(3) # returns 4
# kthLargest.add(5) # returns 5
