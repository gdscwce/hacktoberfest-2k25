from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        
        # DP table: dp[i][j] is the length of LCS of text1[:i] and text2[:j]
        # Using a 2D array:
        # dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # Using O(min(n1, n2)) space optimization (assuming n1 is smaller)
        if n1 < n2:
            return self.longestCommonSubsequence(text2, text1)
            
        # O(n2) space optimization: 'prev' is dp[i-1], 'curr' is dp[i]
        prev = [0] * (n2 + 1) 

        for i in range(1, n1 + 1):
            curr = [0] * (n2 + 1)
            for j in range(1, n2 + 1):
                if text1[i-1] == text2[j-1]:
                    # Match: Take the diagonal value + 1
                    curr[j] = 1 + prev[j-1]
                else:
                    # No match: Take max of top or left
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
            
        return prev[n2]
