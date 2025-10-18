from typing import List

class Solution:
    def _can_make(self, bloomDay: List[int], m: int, k: int, days: int) -> bool:
        """Checks if m bouquets (each of size k) can be made by the given 'days'."""
        bouquet_count = 0
        consecutive_flowers = 0
        
        for day in bloomDay:
            if day <= days:
                # Flower has bloomed, increment consecutive count
                consecutive_flowers += 1
            else:
                # Flower hasn't bloomed, the consecutive sequence is broken
                consecutive_flowers = 0
            
            # If we find k adjacent bloomed flowers, make a bouquet
            if consecutive_flowers == k:
                bouquet_count += 1
                consecutive_flowers = 0 # Reset counter for the next bouquet
                
        return bouquet_count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        
        # 1. Edge Case Check: If total required flowers exceed total available flowers, it's impossible.
        if m * k > n:
            return -1

        # 2. Define the search space for the answer (number of days)
        # The minimum possible day is min(bloomDay), and the maximum is max(bloomDay).
        low = min(bloomDay)
        high = max(bloomDay)
        
        min_days = -1

        # 3. Binary Search on the range of possible days
        while low <= high:
            mid_day = low + (high - low) // 2
            
            # Check if it's possible to make 'm' bouquets by 'mid_day'
            if self._can_make(bloomDay, m, k, mid_day):
                # This day works; store it as a potential answer and try for an earlier day.
                min_days = mid_day
                high = mid_day - 1
            else:
                # This day is too early; need to wait longer.
                low = mid_day + 1
                
        return min_days
