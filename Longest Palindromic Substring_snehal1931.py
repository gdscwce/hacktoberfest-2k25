class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        
        for i in range(len(s)):
            # Odd length palindromes (center is s[i])
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
            
            # Even length palindromes (center is between s[i] and s[i+1])
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
                
        return res
