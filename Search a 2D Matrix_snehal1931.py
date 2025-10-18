def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    M = len(matrix)     # Number of rows
    N = len(matrix[0])  # Number of columns
    
    low = 0
    high = M * N - 1

    while low <= high:
        mid = (low + high) // 2
        
        # Map 1D index 'mid' to 2D coordinates (row, col)
        row = mid // N
        col = mid % N
        
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            # Target is larger, search the right half
            low = mid + 1
        else: # mid_value > target
            # Target is smaller, search the left half
            high = mid - 1
            
    return False

# Example: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 16
# M=3, N=4. Total elements T=12. Range [0, 11]
# Example: mid = 8. row = 8 // 4 = 2. col = 8 % 4 = 0. matrix[2][0] = 23.
# 23 > 16. Search left half: high = 7.
