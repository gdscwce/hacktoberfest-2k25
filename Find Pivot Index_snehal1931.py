from typing import List

def pivotIndex(nums: List[int]) -> int:
    # 1. Calculate the total sum of the array.
    total_sum = sum(nums)
    
    # 2. Initialize the sum of elements to the left of the current index.
    left_sum = 0
    
    # 3. Iterate through the array with index and value.
    for i, num in enumerate(nums):
        
        # Calculate the right sum for the current index i:
        # Right Sum = Total Sum - Left Sum - Current Element (num)
        right_sum = total_sum - left_sum - num
        
        # Check if the current index is a pivot index
        if left_sum == right_sum:
            return i  # Found the leftmost pivot index
        
        # Update the left sum for the next iteration
        left_sum += num
        
    # 4. If the loop finishes without finding a pivot index
    return -1

# Example Usage:
nums1 = [1, 7, 3, 6, 5, 6]
# At index 3: Left Sum (1+7+3)=11, Right Sum (5+6)=11.
print(f"Pivot Index for {nums1}: {pivotIndex(nums1)}")  # Output: 3

nums2 = [1, 2, 3]
# No pivot index exists
print(f"Pivot Index for {nums2}: {pivotIndex(nums2)}")  # Output: -1

nums3 = [2, 1, -1]
# At index 0: Left Sum (0), Right Sum (1 + -1)=0.
print(f"Pivot Index for {nums3}: {pivotIndex(nums3)}")  # Output: 0
