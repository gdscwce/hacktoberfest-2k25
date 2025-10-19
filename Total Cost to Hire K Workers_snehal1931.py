import heapq
from typing import List

class Solution:
    """
    Uses two min-heaps, one for the 'left' candidates and one for the 'right' candidates, 
    to efficiently find the overall lowest-cost worker in each session.
    """
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        # Min-heaps for the two ends
        left_heap = []
        right_heap = []
        
        # Pointers for the first and last available worker index
        left_ptr = 0
        right_ptr = n - 1
        
        total_cost = 0
        
        # Initial population of the heaps
        for _ in range(candidates):
            if left_ptr <= right_ptr:
                heapq.heappush(left_heap, costs[left_ptr])
                left_ptr += 1
            if left_ptr <= right_ptr:
                heapq.heappush(right_heap, costs[right_ptr])
                right_ptr -= 1
        
        # Loop for k hiring sessions
        for _ in range(k):
            # Decide which heap has the minimum cost worker
            # Note: The tie-breaker rule (smallest index) is implicitly handled here:
            # if costs are equal (heap roots are equal), we prioritize left_heap pop, 
            # which ensures the smallest original index (left_ptr is always less than right_ptr).
            
            left_min = left_heap[0] if left_heap else float('inf')
            right_min = right_heap[0] if right_heap else float('inf')
            
            if left_min <= right_min:
                # Hire from the left side
                total_cost += heapq.heappop(left_heap)
                
                # Replenish the left heap if possible
                if left_ptr <= right_ptr:
                    heapq.heappush(left_heap, costs[left_ptr])
                    left_ptr += 1
            else:
                # Hire from the right side
                total_cost += heapq.heappop(right_heap)
                
                # Replenish the right heap if possible
                if left_ptr <= right_ptr:
                    heapq.heappush(right_heap, costs[right_ptr])
                    right_ptr -= 1
        
        return total_cost

# Example Usage:
# sol = Solution()
# sol.totalCost([17,12,10,2,7,2,11,20,8], 3, 4) # returns 11
