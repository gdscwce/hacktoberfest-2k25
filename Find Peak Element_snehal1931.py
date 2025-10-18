from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        # The loop runs until low and high converge to the index of a peak.
        while low < high:
            mid = low + (high - low) // 2
            
            # Compare middle element with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # We are on a descending slope (or at the peak).
                # A peak must be in the left half, including 'mid'.
                high = mid
            else:
                # We are on an ascending slope.
                # A peak must be in the right half, starting at 'mid + 1'.
                low = mid + 1
                
        # When the loop exits, low == high, which is the index of a peak element.
        return low
