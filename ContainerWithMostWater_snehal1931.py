from typing import List

def maxArea(height: List[int]) -> int:
    """
    Finds the maximum amount of water a container can store.
    
    :param height: A list of integers where height[i] is the height of the i-th line.
    :return: The maximum area of water that can be contained.
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the current area: min(height) * width
        current_height = min(height[left], height[right])
        width = right - left
        current_area = current_height * width
        
        # Update the maximum area found so far
        max_area = max(max_area, current_area)
        
        # Move the pointer of the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage:
# height_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(maxArea(height_list))  # Output: 49
