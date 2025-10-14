def decodeString(s: str) -> str:
    # Stack to store the repetition counts
    num_stack = []
    # Stack to store the string built up before the current multiplier/bracket
    str_stack = []
    
    # Variables for the current segment being processed
    curr_num = 0
    curr_str = ""
    
    for char in s:
        if char.isdigit():
            # Handle multi-digit numbers
            curr_num = curr_num * 10 + int(char)
        
        elif char == '[':
            # Save the current state before starting a nested segment
            num_stack.append(curr_num)
            str_stack.append(curr_str)
            
            # Reset for the new segment inside the brackets
            curr_num = 0
            curr_str = ""
        
        elif char == ']':
            # End of a segment: perform the repetition and combine
            num = num_stack.pop()
            prev_str = str_stack.pop()
            
            # The decoded inner string (curr_str * num) is appended to the 
            # outer string (prev_str)
            curr_str = prev_str + curr_str * num
        
        else:
            # Character is a letter
            curr_str += char
            
    return curr_str

# Example Usage:
s1 = "3[a]2[bc]"
# Decodes as: "aaa" + "bc" + "bc" = "aaabcbc"
print(f"'{s1}' decodes to: {decodeString(s1)}")  # Output: aaabcbc

s2 = "3[a2[c]]"
# Decodes as: 3["acc"] = "accaccacc"
print(f"'{s2}' decodes to: {decodeString(s2)}")  # Output: accaccacc

s3 = "2[abc]3[cd]ef"
# Decodes as: "abcabc" + "cdcdcd" + "ef" = "abcabccdcdcdef"
print(f"'{s3}' decodes to: {decodeString(s3)}")  # Output: abcabccdcdcdef
