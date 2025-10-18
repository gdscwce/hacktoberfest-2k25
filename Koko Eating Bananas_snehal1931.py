import math
from typing import List

class Solution:
    # Helper function to calculate the total hours Koko needs for a given speed 'k'
    def _calculate_hours(self, piles: List[int], k: int) -> int:
        total_hours = 0
        for pile in piles:
            # Time to eat a pile is ceil(pile / k). 
            # In Python, you can use math.ceil() or the integer division formula: (pile + k - 1) // k
            total_hours += math.ceil(pile / k)
            # Alternative integer formula: total_hours += (pile + k - 1) // k
            
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. Define the search space for the eating speed 'k'.
        # Minimum possible speed: 1 (Koko must eat at least one)
        low = 1
        
        # Maximum useful speed: max(piles). Eating faster than this won't save time.
        high = max(piles)
        
        # 'res' stores the best (smallest) valid speed found so far.
        res = high 

        # 2. Perform Binary Search
        while low <= high:
            k = low + (high - low) // 2
            
            # Calculate the hours needed for this speed
            hours_needed = self._calculate_hours(piles, k)

            # Check if this speed 'k' is feasible (can finish in time)
            if hours_needed <= h:
                # This speed works! It's a possible answer, so we save it.
                res = k
                # Try to find an even smaller (slower) speed that still works.
                high = k - 1
            else:
                # This speed is too slow; must increase speed.
                low = k + 1
                
        return res
