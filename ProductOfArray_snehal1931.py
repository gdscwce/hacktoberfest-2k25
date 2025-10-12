def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Computes an array where output[i] is the product of all 
    elements of nums except nums[i], without using division 
    and in O(n) time.
    """
    n = len(nums)
    
    # The result array, which will store the final answer
    result = [0] * n
    
    # ----------------------------------------------------
    # 1. Left Pass: Calculate the product of all elements to the LEFT of i.
    # ----------------------------------------------------
    
    # 'current_product' starts at 1, representing the product before the first element.
    current_product = 1
    for i in range(n):
        # result[i] now stores the product of all elements BEFORE nums[i]
        result[i] = current_product
        
        # Update current_product for the next iteration (i.e., include nums[i] 
        # for the product *left* of the next index i+1)
        current_product *= nums[i]
        
    # Example for nums = [1, 2, 3, 4]:
    # i=0: result[0] = 1 (empty product); current_product = 1 * 1 = 1
    # i=1: result[1] = 1 (product of [1]); current_product = 1 * 2 = 2
    # i=2: result[2] = 2 (product of [1, 2]); current_product = 2 * 3 = 6
    # i=3: result[3] = 6 (product of [1, 2, 3]); current_product = 6 * 4 = 24
    # Result after Left Pass: [1, 1, 2, 6]
    
    # ----------------------------------------------------
    # 2. Right Pass: Multiply by the product of all elements to the RIGHT of i.
    # ----------------------------------------------------
    
    # 'current_product' is reset to 1, representing the product after the last element.
    current_product = 1
    # Iterate backward from the last element to the first
    for i in range(n - 1, -1, -1):
        # result[i] currently holds: (Product of Left elements)
        # We multiply it by 'current_product', which holds: (Product of Right elements)
        result[i] *= current_product
        
        # Update current_product for the next iteration (i.e., include nums[i] 
        # for the product *right* of the previous index i-1)
        current_product *= nums[i]

    # Continuing the example for nums = [1, 2, 3, 4] with current result [1, 1, 2, 6]:
    # i=3: result[3] = 6 * 1 = 6; current_product = 1 * 4 = 4
    # i=2: result[2] = 2 * 4 = 8; current_product = 4 * 3 = 12
    # i=1: result[1] = 1 * 12 = 12; current_product = 12 * 2 = 24
    # i=0: result[0] = 1 * 24 = 24; current_product = 24 * 1 = 24
    # Final Result: [24, 12, 8, 6]
    
    return result

# --- Example Usage ---
print(f"Input: [1, 2, 3, 4] -> Output: {productExceptSelf([1, 2, 3, 4])}")
print(f"Input: [-1, 1, 0, -3, 3] -> Output: {productExceptSelf([-1, 1, 0, -3, 3])}")
