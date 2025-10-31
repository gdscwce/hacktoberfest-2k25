class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        return " ".join(l[::-1])
