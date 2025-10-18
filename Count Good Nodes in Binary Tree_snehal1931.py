from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        
        # Define the recursive helper function
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # 1. Check if the current node is a "Good Node"
            # Since the root is always a good node, its value will be >= the max_so_far 
            # passed from the outside (which is correctly initialized to a very small number or the root's value).
            is_good = 0
            if node.val >= max_so_far:
                is_good = 1
            
            # 2. Update the maximum value for the subsequent path
            # The new maximum for the children is the greater of the current node's value 
            # and the inherited maximum.
            new_max = max(max_so_far, node.val)
            
            # 3. Recurse and aggregate the results
            # The total count is: (1 if current node is good) + (good nodes from left) + (good nodes from right)
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        # Start the DFS from the root, initializing max_so_far with the root's value.
        # This ensures the root is counted as the first good node.
        # We can also use float('-inf') if we prefer the logic check to be more general.
        return dfs(root, root.val)
