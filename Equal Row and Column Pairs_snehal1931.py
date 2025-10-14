from typing import List
from collections import Counter

def equalPairs(grid: List[List[int]]) -> int:
    n = len(grid)
    
    # 1. Count the frequency of each unique row.
    # Convert each row (list) to a tuple so it can be hashed (used as a key).
    row_counts = Counter(tuple(row) for row in grid)
    
    equal_pair_count = 0
    
    # 2. Iterate through all columns.
    for j in range(n):
        # Extract the current column's elements.
        current_column = []
        for i in range(n):
            current_column.append(grid[i][j])
            
        # 3. Convert the column to a hashable tuple.
        column_tuple = tuple(current_column)
        
        # Check how many times this column sequence appeared as a row.
        # This is O(1) average time complexity due to the hash map lookup.
        equal_pair_count += row_counts.get(column_tuple, 0)
        
    return equal_pair_count

# Example Usage:
grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
# Rows: (3,2,1):1, (1,7,6):1, (2,7,7):1
# Columns: (3,1,2), (2,7,7), (1,6,7)
# Match: Column (2,7,7) matches Row (2,7,7) once.
print(f"Equal pairs for {grid1}: {equalPairs(grid1)}")  # Output: 1

grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
# Rows: (3,1,2,2):1, (1,4,4,5):1, (2,4,2,2):2
# Columns: (3,1,2,2), (1,4,4,4), (2,4,2,2), (2,5,2,2)
# Matches: Col 0 matches Row 0 (1 pair), Col 2 matches Row 2 & 3 (2 pairs). Total: 3.
print(f"Equal pairs for {grid2}: {equalPairs(grid2)}")  # Output: 3
