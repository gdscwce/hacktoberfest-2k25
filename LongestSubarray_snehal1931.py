from typing import List

def longestSubarray(nums: List[int]) -> int:
    left = 0
    zero_count = 0
    max_len = 0
    
    # The right pointer 'r' expands the window
    for r in range(len(nums)):
        
        # 1. Expand Window: Count the zeros
        if nums[r] == 0:
            zero_count += 1
        
        # 2. Shrink Window: If we have more than one zero
        while zero_count > 1:
            # If the element leaving the window is a zero, decrement the count
            if nums[left] == 0:
                zero_count -= 1
            
            # Shrink the window by moving the left pointer
            left += 1
            
        # 3. Track Maximum Length
        # The window size is (r - left + 1). Since we must delete one element
        # (which is either the single zero or a one), the resulting subarray
        # of 1's has a length of (window size - 1).
        # Length of consecutive 1s = (r - left + 1) - 1 = r - left
        max_len = max(max_len, r - left)
        
    return max_len
