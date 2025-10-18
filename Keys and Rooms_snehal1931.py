import collections

class Solution:
    def canVisitAllRooms_bfs(self, rooms: list[list[int]]) -> bool:
        # A set to keep track of visited rooms
        visited = {0}
        
        # A deque for BFS (queue), starting with room 0
        queue = collections.deque([0])
        
        while queue:
            room = queue.popleft()
            
            # The keys are the neighbors (other rooms we can visit)
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        
        # If the number of visited rooms equals the total number of rooms, we can visit all.
        return len(visited) == len(rooms)
