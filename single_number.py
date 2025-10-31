# ==============================================
# Project: Single Number
# Language: Python 3
# Description:
#   Given a non-empty array of integers, every element appears twice
#   except for one. Find that single one using XOR logic.
# ==============================================

from typing import List

class SingleNumberFinder:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # XOR cancels out duplicate numbers
            result ^= num
        return result


if __name__ == "__main__":
    finder = SingleNumberFinder()

    print("=============================================")
    print("               SINGLE NUMBER PROJECT")
    print("=============================================")

    nums = [4, 1, 2, 1, 2]
    print("Input:", nums)
    print("Single Number Found:", finder.singleNumber(nums))

    print("\nProgram completed successfully!")
