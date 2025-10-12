def moveZeroes(nums: list[int]) -> None:
    """
    Moves all zeroes to the end of the array in-place while maintaining 
    the relative order of the non-zero elements.
    
    :param nums: The list of integers to be modified.
    :return: None (the modification is done in-place).
    """
    
    # 'non_zero_ptr' tracks the position where the next non-zero element should be placed.
    non_zero_ptr = 0
    
    # 1. Iterate through the array with 'i' (the reader pointer).
    for i in range(len(nums)):
        
        # If the element at the current position 'i' is NOT zero:
        if nums[i] != 0:
            
            # Place the non-zero element at the position tracked by 'non_zero_ptr'.
            # This is essentially moving all non-zero elements to the front of the array.
            nums[non_zero_ptr] = nums[i]
            
            # Increment 'non_zero_ptr' to point to the next empty slot 
            # (which will eventually be filled with a zero or the next non-zero number).
            non_zero_ptr += 1

    # 2. Fill the remaining slots with zeroes.
    # After the first loop, 'non_zero_ptr' points to the first position 
    # where a zero should be placed (the end of the non-zero elements).
    for i in range(non_zero_ptr, len(nums)):
        nums[i] = 0

# --- Example Usage ---
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(f"Input: [0, 1, 0, 3, 12] -> Output: {nums1}") 
# Expected Output: [1, 3, 12, 0, 0]

nums2 = [0]
moveZeroes(nums2)
print(f"Input: [0] -> Output: {nums2}") 
# Expected Output: [0]

nums3 = [1, 2, 3]
moveZeroes(nums3)
print(f"Input: [1, 2, 3] -> Output: {nums3}") 
# Expected Output: [1, 2, 3]
