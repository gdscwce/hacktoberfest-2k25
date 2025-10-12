def reverseWords(s: str) -> str:
    """
    Reverses the order of words in a string.
    
    The function handles leading, trailing, and multiple spaces 
    between words by automatically filtering empty strings 
    during the split operation.
    """
    
    # 1. Split the string by whitespace. 
    #    The split() method without arguments automatically handles 
    #    multiple spaces and filters out empty strings.
    words = s.split()
    
    # 2. Reverse the list of words.
    words.reverse()
    
    # 3. Join the reversed list of words back into a single string 
    #    using a single space (' ') as the separator.
    return " ".join(words)

# --- Example Usage ---
print(f"'the sky is blue' -> '{reverseWords('the sky is blue')}'")
print(f"'  hello world  ' -> '{reverseWords('  hello world  ')}'")
print(f"'a good   example' -> '{reverseWords('a good   example')}'")
print(f"'y' -> '{reverseWords('y')}'")
