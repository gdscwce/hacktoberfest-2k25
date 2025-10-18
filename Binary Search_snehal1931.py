def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate midpoint
        mid = left + (right - left) // 2
        
        # Check if the target is found
        if arr[mid] == target:
            return mid
        
        # Target is in the right half
        elif arr[mid] < target:
            left = mid + 1
        
        # Target is in the left half
        else: # arr[mid] > target
            right = mid - 1
            
    # Target was not found in the array
    return -1

# Example
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23
index = binary_search(data, target_val)

if index != -1:
    print(f"Target {target_val} found at index: {index}") # Output: Target 23 found at index: 5
else:
    print(f"Target {target_val} not found.")
