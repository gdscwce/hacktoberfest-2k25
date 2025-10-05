from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()       # Right-moving asteroid destroyed
                    continue
                elif stack[-1] == -a:
                    stack.pop()       # Both destroyed
                break
            else:
                stack.append(a)
        return stack
