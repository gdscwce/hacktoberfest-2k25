from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    
    for new_asteroid in asteroids:
        # Loop handles potential chain reactions of collisions
        while stack and new_asteroid < 0 and stack[-1] > 0:
            
            # Case 1: Stack-top asteroid is smaller (it explodes)
            if stack[-1] < abs(new_asteroid):
                stack.pop()
                continue  # Continue collision check against the next asteroid on the stack
            
            # Case 2: Both are the same size (both explode)
            elif stack[-1] == abs(new_asteroid):
                stack.pop()
                new_asteroid = 0  # Mark current asteroid as destroyed
                break  # Stop checking collisions for this now-destroyed asteroid
            
            # Case 3: Stack-top asteroid is larger (new_asteroid explodes)
            else: # stack[-1] > abs(new_asteroid)
                new_asteroid = 0  # Mark current asteroid as destroyed
                break  # Stop checking collisions
                
        # If the new_asteroid was not destroyed (it is not 0), add it to the stack.
        # This covers: right-movers (+), left-movers (-) that survive, and 
        # left-movers that encounter an empty stack or a left-mover on top.
        if new_asteroid != 0:
            stack.append(new_asteroid)
            
    return stack

# Example Usage:
print(f"Result for [5, 10, -5]: {asteroidCollision([5, 10, -5])}")   # Output: [5, 10]
print(f"Result for [10, 2, -5]: {asteroidCollision([10, 2, -5])}")   # Output: [10, -5] -> 2 and -5 collide, -5 survives. Then 10 and -5 never collide. [10, -5]
print(f"Result for [8, -8]: {asteroidCollision([8, -8])}")           # Output: []
print(f"Result for [-2, -1, 1, 2]: {asteroidCollision([-2, -1, 1, 2])}") # Output: [-2, -1, 1, 2] (no collisions possible)
