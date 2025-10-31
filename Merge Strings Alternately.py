class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w=""
        i=0
        def maxw(word1,word2):
            if len(word1)>=len(word2):
                return word1
            else:
                return word2
        wl=maxw(word1,word2)
        while True:
            if i<len(word1) and i<len(word2):
                w=w+word1[i]+word2[i]
                i+=1
            elif i<len(wl):
                w=w+wl[i:]
                break
            else:
                break
            
        return w
