from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # DP approach: dp[i] = dp[i / 2] + (i % 2)
        
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i >> 1 is equivalent to i // 2
            # i & 1 is equivalent to i % 2
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans
