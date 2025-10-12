from typing import Set

def maxVowels(s: str, k: int) -> int:
    # 1. Define vowels for O(1) lookup
    VOWELS: Set[str] = {'a', 'e', 'i', 'o', 'u'}
    
    # Helper to check if a character is a vowel (returns 1 or 0)
    is_vowel = lambda char: 1 if char in VOWELS else 0

    # 2. Calculate initial count for the first window (s[0] to s[k-1])
    current_count = sum(is_vowel(s[i]) for i in range(k))
    max_count = current_count
    
    # Check for early exit if we've already hit the maximum possible vowels
    if max_count == k:
        return k

    # 3. Slide the window
    n = len(s)
    for i in range(k, n):
        # Update the count by adjusting for the character leaving and the one entering
        
        # Character leaving the window is at index i - k
        current_count -= is_vowel(s[i - k])
        
        # New character entering the window is at index i
        current_count += is_vowel(s[i])
        
        # Update the maximum count
        max_count = max(max_count, current_count)
        
        # Optional: Early termination
        if max_count == k:
            return k

    # 4. Return the result
    return max_count

# Example: s = "abciiidef", k = 3
# Initial (i=0 to 2): "abc", current_count = 1, max_count = 1
# i=3: Leaving 'a' (-1), Entering 'i' (+1). current_count = 1. max_count = 1
# i=4: Leaving 'b' (0), Entering 'i' (+1). current_count = 2. max_count = 2
# i=5: Leaving 'c' (0), Entering 'i' (+1). current_count = 3. max_count = 3 -> RETURNS 3
