from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is the minimum number of coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # 0 coins needed for amount 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    # If we can use this coin, update dp[a]
                    # The number of coins is 1 (for current coin) + min coins for remaining amount (a - coin)
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                    
        # If dp[amount] is still infinity, it's impossible to make the amount
        return dp[amount] if dp[amount] != float('inf') else -1
