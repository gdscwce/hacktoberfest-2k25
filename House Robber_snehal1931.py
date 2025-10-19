from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP approach with O(1) space
        
        # Base cases
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        # dp_i_minus_2: max profit ending at house i-2
        # dp_i_minus_1: max profit ending at house i-1
        
        dp_i_minus_2 = nums[0] # Max profit up to house 0
        dp_i_minus_1 = max(nums[0], nums[1]) # Max profit up to house 1

        for i in range(2, len(nums)):
            # Max profit for current house i is:
            # 1. Rob house i: nums[i] + (max profit up to i-2)
            # 2. Skip house i: (max profit up to i-1)
            dp_i = max(nums[i] + dp_i_minus_2, dp_i_minus_1)
            
            dp_i_minus_2 = dp_i_minus_1
            dp_i_minus_1 = dp_i
            
        return dp_i_minus_1
