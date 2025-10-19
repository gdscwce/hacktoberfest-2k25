class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        # Helper function to count palindromes expanding from a center
        def expand_and_count(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            # Odd length palindromes (center s[i])
            expand_and_count(i, i)
            
            # Even length palindromes (center between s[i] and s[i+1])
            expand_and_count(i, i + 1)
            
        return count
