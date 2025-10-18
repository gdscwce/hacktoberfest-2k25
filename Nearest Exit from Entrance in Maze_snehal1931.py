import collections

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_row, start_col = entrance[0], entrance[1]
        
        # Directions: (row_change, col_change) for up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Queue stores tuples of (row, col)
        queue = collections.deque([(start_row, start_col)])
        
        # To track steps (distance from the start)
        steps = 0
        
        # Mark the entrance as visited to prevent revisiting and to ensure 
        # it is not counted as an exit, even if it is on the border.
        maze[start_row][start_col] = '+' 

        while queue:
            steps += 1
            # Process all cells at the current distance level
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                
                # Check neighbors
                for dr, dc in directions:
                    next_row, next_col = curr_row + dr, curr_col + dc
                    
                    # 1. Check if the new position is within bounds
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        
                        # 2. Check if the cell is an empty path ('.') and hasn't been visited ('+')
                        if maze[next_row][next_col] == '.':
                            
                            # 3. Check if it is an EXIT (on the border)
                            is_on_border = (next_row == 0 or next_row == rows - 1 or 
                                            next_col == 0 or next_col == cols - 1)
                            
                            if is_on_border:
                                # BFS guarantee: the first exit found is the nearest
                                return steps
                            
                            # If it's not the exit, add it to the queue and mark as visited
                            maze[next_row][next_col] = '+'
                            queue.append((next_row, next_col))
                            
        # If the queue empties and no exit was found
        return -1
