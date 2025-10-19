from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Finds all combinations of k unique numbers (1-9) that sum up to n.
        """
        res = []
        
        def backtrack(start_num, current_sum, combination):
            # Base Case 1: If combination has k elements
            if len(combination) == k:
                if current_sum == n:
                    res.append(list(combination))
                return
            
            # Optimization: If sum exceeds n, stop early
            if current_sum > n:
                return

            # Recursive step: try numbers from start_num to 9
            for num in range(start_num, 10):
                combination.append(num)
                # Recurse with the next number (num + 1) and updated sum
                backtrack(num + 1, current_sum + num, combination)
                combination.pop() # Backtrack

        # Start checking numbers from 1, initial sum is 0, combination is empty
        backtrack(1, 0, [])
        return res
