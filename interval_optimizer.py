# ==============================================
# Project: Interval Optimizer
# Features: 
#   1. Remove Overlapping Intervals
#   2. Find Minimum Number of Arrows to Burst Balloons
# Language: Python 3
# ==============================================

from typing import List

class IntervalOptimizer:
    # ----------------------------------------------
    # Problem 1: Non-overlapping Intervals
    # Goal: Find the minimum number of intervals to remove
    # ----------------------------------------------
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their ending time
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # Overlapping interval -> remove it
                count += 1
            else:
                # Move to next non-overlapping interval
                end = intervals[i][1]
        return count

    # ----------------------------------------------
    # Problem 2: Minimum Number of Arrows to Burst Balloons
    # Goal: Find the least number of arrows needed
    # ----------------------------------------------
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort by the end coordinate
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > end:
                # Need a new arrow
                arrows += 1
                end = points[i][1]
        return arrows


# ===============================================
# Main Function for Demonstration
# ===============================================
if __name__ == "__main__":
    optimizer = IntervalOptimizer()

    print("===============================================")
    print("        INTERVAL OPTIMIZER PROJECT")
    print("===============================================\n")

    # ---- Example 1: Non-overlapping Intervals ----
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print("Example 1: Non-overlapping Intervals")
    print("Input Intervals:", intervals)
    result1 = optimizer.eraseOverlapIntervals(intervals)
    print("Minimum Intervals to Remove:", result1, "\n")

    # ---- Example 2: Minimum Arrows ----
    points = [[10,16],[2,8],[1,6],[7,12]]
    print("Example 2: Minimum Number of Arrows")
    print("Input Balloons:", points)
    result2 = optimizer.findMinArrowShots(points)
    print("Minimum Arrows Needed:", result2)

    print("\n===============================================")
    print("Program Completed Successfully!")
    print("===============================================")
