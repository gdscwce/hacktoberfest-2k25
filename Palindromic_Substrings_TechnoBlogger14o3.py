"""
LeetCode 75: Palindromic Substrings

Problem Statement:
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Time Complexity: O(n^2)
Space Complexity: O(1)

Approach:
1. Use expand around centers technique
2. For each possible center (single character or between two characters)
3. Expand outward while characters match
4. Count all valid palindromes found

@author TechnoBlogger14o3
@date 2025
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count palindromic substrings using expand around centers.
        
        Args:
            s: Input string
            
        Returns:
            Number of palindromic substrings
        """
        count = 0
        n = len(s)
        
        # Expand around each possible center
        for i in range(n):
            # Odd length palindromes (center at i)
            count += self.expand_around_center(s, i, i)
            
            # Even length palindromes (center between i and i+1)
            count += self.expand_around_center(s, i, i + 1)
        
        return count
    
    def expand_around_center(self, s: str, left: int, right: int) -> int:
        """
        Expand around center and count palindromes.
        
        Args:
            s: Input string
            left: Left boundary
            right: Right boundary
            
        Returns:
            Number of palindromes found
        """
        count = 0
        n = len(s)
        
        # Expand while characters match and boundaries are valid
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count


# Alternative approach using dynamic programming
class SolutionDP:
    def countSubstrings(self, s: str) -> int:
        """
        Count palindromic substrings using dynamic programming.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        
        # Check for palindromes of length 3 and more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
        
        return count


"""
Test Cases:
- "abc" → 3
- "aaa" → 6
- "racecar" → 10
- "a" → 1
- "" → 0

Key Insights:
- Every single character is a palindrome
- We need to check both odd and even length palindromes
- Expand around centers is more space efficient than DP
- DP approach is easier to understand but uses more memory

Performance Comparison:
- Expand around centers: O(n^2) time, O(1) space
- Dynamic programming: O(n^2) time, O(n^2) space
"""
