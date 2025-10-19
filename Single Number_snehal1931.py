from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR property: a ^ a = 0 and a ^ 0 = a.
        # XORing all numbers will cancel out all pairs, leaving the single number.
        
        result = 0
        for num in nums:
            result ^= num
        return result
