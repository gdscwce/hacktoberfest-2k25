from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # DP state:
        # hold: max profit ending at day i with a stock in hand (bought at some point)
        # cash: max profit ending at day i with no stock in hand (sold or no operation)
        
        # Initial states (Day 0)
        cash = 0
        hold = -prices[0] # To hold a stock, you must buy it (cost: prices[0])

        for i in range(1, len(prices)):
            new_cash = max(
                cash,                   # 1. No operation (stayed in cash)
                hold + prices[i] - fee  # 2. Sell today (transition from hold to cash)
            )
            
            new_hold = max(
                hold,                   # 1. No operation (stayed in hold)
                cash - prices[i]        # 2. Buy today (transition from cash to hold)
            )
            
            cash = new_cash
            hold = new_hold
            
        # Final answer is the max profit when we end up with cash
        return cash
