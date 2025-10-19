from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all subsets using a recursive backtracking approach.
        """
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                # Base case: we've processed all elements
                res.append(list(subset))
                return

            # 1. Decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # 2. Decision to NOT include nums[i] (backtrack)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
