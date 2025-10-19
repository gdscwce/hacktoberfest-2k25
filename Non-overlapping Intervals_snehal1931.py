from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Finds the minimum number of intervals to remove to make the rest non-overlapping.
        This is equivalent to finding the maximum number of non-overlapping intervals.
        """
        if not intervals:
            return 0
            
        # Greedy choice: Sort by the END TIME of the intervals.
        # This ensures that when we pick an interval, it finishes as early as possible, 
        # leaving the maximum room for the remaining intervals.
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end_time = float('-inf')

        for start, end in intervals:
            if start >= end_time:
                # The current interval does not overlap with the last chosen one.
                # Choose this interval and update the end time.
                end_time = end
            else:
                # Overlap detected. This interval must be removed.
                count += 1
                
        # Total intervals to remove = total - max_non_overlapping_intervals
        # The return value is the count of intervals *removed*.
        return count
