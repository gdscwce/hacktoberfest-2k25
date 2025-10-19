import heapq

class SmallestInfiniteSet:
    """
    Keeps track of numbers that were popped and added back using a min-heap,
    and the smallest *next* unpopped number using a simple integer counter.
    """
    def __init__(self):
        # Min-heap to store numbers added back
        self.added_back = [] 
        # Smallest number not yet popped from the infinite set
        self.smallest_unpopped = 1 

    def popSmallest(self) -> int:
        if self.added_back:
            # If there are numbers added back, the smallest is the root of the min-heap
            return heapq.heappop(self.added_back)
        else:
            # Otherwise, the smallest is the next unpopped number
            result = self.smallest_unpopped
            self.smallest_unpopped += 1
            return result

    def addBack(self, num: int) -> None:
        # Only add back if the number is smaller than the smallest_unpopped
        # and it's not already in the added_back set (use a set for O(1) check if possible, 
        # or rely on the logic that only *removed* numbers are candidates for addBack)
        
        # A simpler, more robust approach is to maintain a set of numbers that *are* # in the heap to check for duplicates, or only allow adding back numbers 
        # strictly less than self.smallest_unpopped and not already in the heap.
        
        # Assuming the standard LeetCode constraint where 'num' is only added back 
        # if it was previously removed, and we need to avoid duplicates in the heap.
        if num < self.smallest_unpopped and num not in self.added_back:
            heapq.heappush(self.added_back, num)

# Example Usage:
# obj = SmallestInfiniteSet()
# obj.popSmallest() # returns 1
# obj.addBack(2) 
# obj.popSmallest() # returns 2 (as 2 was the smallest unpopped or added back)
