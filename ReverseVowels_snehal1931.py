def reverseVowels(s: str) -> str:
    """
    Reverses only the vowels in a string.
    Vowels are 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.
    """
    
    # 1. Convert the string to a list of characters for mutable operations
    s_list = list(s)
    
    # 2. Define the set of vowels for quick lookups (O(1) average time complexity)
    VOWELS = set('aeiouAEIOU')
    
    # 3. Initialize two pointers: 'left' at the start and 'right' at the end
    left, right = 0, len(s_list) - 1
    
    # 4. Use a two-pointer approach to find and swap vowels
    while left < right:
        
        # Move 'left' pointer until it finds a vowel
        while left < right and s_list[left] not in VOWELS:
            left += 1
            
        # Move 'right' pointer until it finds a vowel
        while left < right and s_list[right] not in VOWELS:
            right -= 1
            
        # If both pointers found vowels and haven't crossed, swap them
        if left < right:
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # Move both pointers inward
            left += 1
            right -= 1
            
    # 5. Join the list back into a string and return it
    return "".join(s_list)

# --- Example Usage ---
print(f"hello -> {reverseVowels('hello')}")         # Output: holle
print(f"leetcode -> {reverseVowels('leetcode')}")   # Output: leotcede
print(f"aA -> {reverseVowels('aA')}")               # Output: Aa
print(f"design -> {reverseVowels('design')}")       # Output: diseng
