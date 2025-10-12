def compress(chars: list[str]) -> int:
    """
    Compresses a list of characters in-place and returns the new length.
    
    The compression replaces consecutive repeating characters with the 
    character and the count of its repetitions (if the count > 1).
    """
    
    # 'anchor' marks the start of the current group of repeating characters.
    anchor = 0
    
    # 'write' is the index where the compressed output is written in the array.
    write = 0
    
    # 'read' iterates through the original array.
    n = len(chars)
    
    for read in range(n):
        # Check if we are at the end of the array OR the current character 
        # is different from the next one. This marks the END of a group.
        if read + 1 == n or chars[read + 1] != chars[read]:
            
            # --- 1. Write the character ---
            # The character is the one at the start of the current group (anchor).
            chars[write] = chars[anchor]
            write += 1
            
            # --- 2. Calculate and Write the count (if > 1) ---
            count = read - anchor + 1
            
            if count > 1:
                # Convert the count into a string and iterate through its digits.
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            # --- 3. Move the anchor to the next group's start ---
            anchor = read + 1
            
    # 'write' now holds the new length of the compressed array
    return write

# --- Example Usage ---
chars1 = ["a", "a", "b", "b", "c", "c", "c"]
length1 = compress(chars1)
print(f"Input: {['a', 'a', 'b', 'b', 'c', 'c', 'c']}")
print(f"Compressed length: {length1}")
print(f"Compressed array (first {length1} elements): {chars1[:length1]}") 
# Output: ["a", "2", "b", "2", "c", "3"]

chars2 = ["a"]
length2 = compress(chars2)
print(f"\nInput: {['a']}")
print(f"Compressed length: {length2}")
print(f"Compressed array (first {length2} elements): {chars2[:length2]}")
# Output: ["a"]

chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
length3 = compress(chars3)
print(f"\nInput: {['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']}")
print(f"Compressed length: {length3}")
print(f"Compressed array (first {length3} elements): {chars3[:length3]}")
# Output: ["a", "b", "1", "2"]
