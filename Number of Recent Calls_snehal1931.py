from collections import deque

class RecentCounter:
    
    def __init__(self):
        # Initialize a deque (double-ended queue) to store timestamps.
        # This will hold all recent call times in increasing order.
        self.request_times = deque() 
        
    def ping(self, t: int) -> int:
        """
        Adds a new request at time t and returns the count of requests
        in the range [t - 3000, t].
        """
        # 1. Add the new request timestamp to the end of the queue.
        self.request_times.append(t)
        
        # 2. Define the starting time for the 3000ms window.
        window_start_time = t - 3000
        
        # 3. Remove all outdated requests from the front of the queue.
        # The oldest request is at the front (index 0). 
        # Since 't' is strictly increasing, we only check the front element.
        while self.request_times and self.request_times[0] < window_start_time:
            self.request_times.popleft()
            
        # 4. The size of the remaining queue is the number of recent calls.
        return len(self.request_times)

# Example Usage:
# recentCounter = RecentCounter()
# print(recentCounter.ping(1))    # Output: 1  (range [-2999, 1])
# print(recentCounter.ping(100))  # Output: 2  (range [-2900, 100])
# print(recentCounter.ping(3001)) # Output: 3  (range [1, 3001])
# print(recentCounter.ping(3002)) # Output: 3  (range [2, 3002] - time 1 is removed)
