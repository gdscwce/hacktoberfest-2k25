from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Finds the minimum number of arrows required to burst all balloons.
        This is equivalent to finding the maximum number of non-overlapping intervals (rephrased).
        """
        if not points:
            return 0
            
        # Greedy choice: Sort by the END coordinate of the balloons.
        # This makes it easier to determine the optimal shot location.
        points.sort(key=lambda x: x[1])
        
        arrow_count = 0
        last_arrow_pos = float('-inf')

        for start, end in points:
            if start > last_arrow_pos:
                # The current balloon is outside the range of the last arrow shot.
                # We need a new arrow, shot at the end of the current balloon (greedy choice).
                arrow_count += 1
                last_arrow_pos = end
                
        return arrow_count
