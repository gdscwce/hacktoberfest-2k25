from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    # 'l' is the left pointer (start of the window)
    l = 0
    
    # 'r' is the right pointer (loop variable, end of the window)
    for r in range(len(nums)):
        # 1. Expand Window & Update Constraint
        # If the new element is 0, we use one of our allowed flips (k).
        if nums[r] == 0:
            k -= 1
        
        # 2. Shrink Window (when constraint is violated: k < 0)
        # If k becomes negative, it means we have too many zeros in the window.
        if k < 0:
            # Check the element leaving the window (nums[l]). 
            # If it's a 0, we 'free up' a flip count by moving past it.
            if nums[l] == 0:
                k += 1  # Increment k, meaning we regain a flip allowance
            
            # Always move the left pointer forward to shrink the window
            l += 1
            
    # 3. Calculate Maximum Length
    # After the loop, the window [l:r] is the longest valid window found.
    # The length is r - l + 1. Since 'r' stops at len(nums) - 1, the true length
    # is len(nums) - l.
    return len(nums) - l
