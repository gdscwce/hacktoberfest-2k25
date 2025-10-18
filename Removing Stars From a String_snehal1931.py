def removeStars(s: str) -> str:
    """
    Removes stars and the closest preceding non-star character.
    """
    stack = []
    for char in s:
        if char == '*':
            # If stack is not empty, pop the last non-star character
            if stack:
                stack.pop() 
        else:
            # Add non-star characters to the stack
            stack.append(char) 
            
    # Join the remaining characters in the stack to form the final string
    return "".join(stack)

# Example 1:
s1 = "leet**cod*e"
# 'l'->stack:['l']
# 'e'->stack:['l', 'e']
# 'e'->stack:['l', 'e', 'e']
# 't'->stack:['l', 'e', 'e', 't']
# '*'->pop('t')->stack:['l', 'e', 'e']
# '*'->pop('e')->stack:['l', 'e']
# 'c'->stack:['l', 'e', 'c']
# 'o'->stack:['l', 'e', 'c', 'o']
# 'd'->stack:['l', 'e', 'c', 'o', 'd']
# '*'->pop('d')->stack:['l', 'e', 'c', 'o']
# 'e'->stack:['l', 'e', 'c', 'o', 'e']
print(f"Input: {s1}, Output: {removeStars(s1)}") 
# Output: Input: leet**cod*e, Output: lecoe

# Example 2:
s2 = "erase*****"
# 'e'->['e'], 'r'->['e','r'], 'a'->['e','r','a'], 's'->['e','r','a','s'], 'e'->['e','r','a','s','e']
# *->pop('e')
# *->pop('s')
# *->pop('a')
# *->pop('r')
# *->pop('e')
print(f"Input: {s2}, Output: {removeStars(s2)}") 
# Output: Input: erase*****, Output:
