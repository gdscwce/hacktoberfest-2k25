import collections
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0  # Or handle as per problem constraints, usually root is not None

        # Use a deque for efficient appends and poplefts (queue operations)
        queue = collections.deque([root])
        
        # Initialize tracking variables
        max_sum = -math.inf  # Start with negative infinity to correctly handle negative node values
        max_level = 0
        current_level = 1
        
        while queue:
            # Get the size of the current level's nodes in the queue
            level_size = len(queue)
            level_sum = 0
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Check if the current level sum is the new maximum
            # We use strict inequality (>) to ensure we get the smallest level index
            # if multiple levels have the same maximum sum.
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            # Move to the next level
            current_level += 1
            
        return max_level

# Example Usage:
# Construct the tree [1, 7, 0, 7, -8, null, null]
# Level 1: 1
# Level 2: 7 + 0 = 7
# Level 3: 7 + -8 = -1
# Max sum is 7 at level 2.

# root = TreeNode(1,
#                 TreeNode(7, TreeNode(7), TreeNode(-8)),
#                 TreeNode(0))
# print(Solution().maxLevelSum(root)) # Output: 2
