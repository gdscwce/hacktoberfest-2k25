from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        res = []

        def backtrack(index, current_combination):
            # Base Case: processed all digits
            if index == len(digits):
                res.append("".join(current_combination))
                return

            # Get the letters for the current digit
            digit = digits[index]
            letters = mapping[digit]

            # Recurse for each possible letter
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop() # Backtrack

        backtrack(0, [])
        return res
