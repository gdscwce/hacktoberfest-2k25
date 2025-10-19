from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] is the minimum cost to reach step i
        
        # We only need the previous two results, so we can use O(1) space.
        
        # min cost to reach step 0 (after paying cost[0])
        dp_i_minus_2 = cost[0] 
        # min cost to reach step 1 (after paying cost[1])
        dp_i_minus_1 = cost[1]
        
        for i in range(2, n):
            # To reach step i, we can come from i-1 or i-2.
            # The cost paid at step i is cost[i].
            dp_i = cost[i] + min(dp_i_minus_1, dp_i_minus_2)
            
            # Shift variables for the next iteration
            dp_i_minus_2 = dp_i_minus_1
            dp_i_minus_1 = dp_i
            
        # The final answer is the min cost to reach step n-1 or step n-2
        # (since we can jump from either to the top/destination).
        return min(dp_i_minus_1, dp_i_minus_2)
