from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    # 1. Calculate the initial sum of the first window (length k)
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    n = len(nums)
    
    # 2. Slide the window from index k to the end of the array
    for i in range(k, n):
        # Update current_sum: Add new element and subtract the element leaving the window
        current_sum = current_sum + nums[i] - nums[i - k]
        
        # Update the maximum sum found
        max_sum = max(max_sum, current_sum)
        
    # 3. Calculate and return the maximum average
    # Use float conversion for accurate division, although Python 3's '/' performs float division
    return max_sum / k

# Example Usage:
# nums = [1, 12, -5, -6, 50, 3], k = 4
# Initial window: [1, 12, -5, -6], current_sum = 2, max_sum = 2
# i = 4: current_sum = 2 - 1 + 50 = 51. max_sum = 51
# i = 5: current_sum = 51 - 12 + 3 = 42. max_sum = 51
# Result: 51 / 4 = 12.75
