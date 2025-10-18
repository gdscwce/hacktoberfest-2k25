import collections

class Solution:
    def minReorder_bfs(self, n: int, connections: list[list[int]]) -> int:
        # Build the Adjacency List (same as DFS)
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1)) # Original: u -> v (cost 1 to move u->v)
            graph[v].append((u, 0)) # Reverse: v <- u (cost 0 to move v->u)
            
        reversals = 0
        queue = collections.deque([0]) # Start BFS at city 0
        visited = {0}

        while queue:
            city = queue.popleft()
            
            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
                    # If cost is 1, the edge was originally 'city -> neighbor',
                    # meaning it points away from our starting point (city 0)
                    # and must be reversed.
                    reversals += cost

        return reversals
