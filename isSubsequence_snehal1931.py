def isSubsequence(s: str, t: str) -> bool:
    """
    Checks if string 's' is a subsequence of string 't'.
    This is achieved using a two-pointer approach, which is O(len(t)) time complexity.
    """
    
    # Base case: An empty string 's' is always a subsequence of any 't'.
    if not s:
        return True
    
    # Initialize pointers for both strings
    s_ptr = 0  # Pointer for the potential subsequence 's'
    t_ptr = 0  # Pointer for the main string 't'
    
    len_s = len(s)
    len_t = len(t)
    
    # Iterate through the main string 't'
    while t_ptr < len_t:
        
        # Check if the characters at the current pointers match
        if s[s_ptr] == t[t_ptr]:
            # Found a match! Move the 's' pointer forward.
            s_ptr += 1
            
            # If s_ptr has reached the end of 's', we've found all characters 
            # in the correct order, so 's' is a subsequence.
            if s_ptr == len_s:
                return True
        
        # In every iteration (match or no match), we must advance the 't' pointer 
        # to continue searching in the main string.
        t_ptr += 1
        
    # If the loop finishes (t_ptr reaches the end of 't') but s_ptr has not 
    # reached the end of 's', it means we did not find all characters of 's'.
    return s_ptr == len_s

# --- Example Usage ---
print(f"s='abc', t='ahbgdc' -> {isSubsequence('abc', 'ahbgdc')}")     # True
print(f"s='axc', t='ahbgdc' -> {isSubsequence('axc', 'ahbgdc')}")     # False
print(f"s='', t='ahbgdc' -> {isSubsequence('', 'ahbgdc')}")           # True
print(f"s='ace', t='abcde' -> {isSubsequence('ace', 'abcde')}")       # True
print(f"s='aec', t='abcde' -> {isSubsequence('aec', 'abcde')}")       # False
