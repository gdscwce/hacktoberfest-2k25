import collections

class Solution:
    def findCircleNum_bfs(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        queue = collections.deque()

        # Iterate through every city
        for i in range(n):
            if not visited[i]:
                # Found the starting point of a new, unvisited province
                provinces += 1
                
                # Start BFS traversal
                queue.append(i)
                visited[i] = True
                
                while queue:
                    city = queue.popleft()
                    
                    # Check all other cities (neighbors)
                    for neighbor in range(n):
                        # Check if 'neighbor' is connected to 'city' and is unvisited
                        if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            
        return provinces
