from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] is the number of combinations to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1 # 1 way to make amount 0 (by choosing no coins)
        
        # Iterate over coins first (to ensure combinations are not permutations)
        for coin in coins:
            # Iterate from coin up to amount
            for a in range(coin, amount + 1):
                # The number of ways to make amount 'a' is increased by the number of 
                # ways to make the remaining amount 'a - coin'.
                dp[a] += dp[a - coin]
                
        return dp[amount]
