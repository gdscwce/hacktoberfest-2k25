import collections

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # graph[A][B] := A / B (stores the weight of the directed edge A -> B)
        graph = collections.defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            # A / B = value
            graph[A][B] = value
            # B / A = 1 / value
            graph[B][A] = 1.0 / value
            
        # The result list
        results = []
        
        # ----------------------------------------------------
        
        def dfs(start: str, end: str, current_product: float, visited: set) -> float:
            """
            Recursively finds the product (value of start / end) along a path.
            """
            # 1. Base Case: The destination is reached
            if start == end:
                return current_product
            
            visited.add(start)
            
            # 2. Explore Neighbors
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    # Recursive call: find the product for neighbor / end
                    # The product accumulated so far is (start / neighbor) * (neighbor / end)
                    result = dfs(neighbor, end, current_product * value, visited)
                    
                    # If the result is valid (not -1.0), return the found value
                    if result != -1.0:
                        return result
            
            # 3. Backtrack (remove start from visited for other queries, although unnecessary for the top call)
            # This is technically optional for the overall algorithm's correctness 
            # if a fresh set is passed for each query, but good practice for path finding.
            visited.remove(start) 
            return -1.0 # Path not found from this branch

        # ----------------------------------------------------
        
        # 3. Process Queries
        for A, C in queries:
            # Handle non-existent variables
            if A not in graph or C not in graph:
                results.append(-1.0)
            # Handle the case where A and C exist in the graph and a path might exist
            else:
                # Start DFS with an initial product of 1.0 and a new visited set
                result = dfs(A, C, 1.0, set())
                results.append(result)
                
        return results
