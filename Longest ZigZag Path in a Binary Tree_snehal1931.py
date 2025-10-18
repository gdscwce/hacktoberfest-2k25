from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Variable to store the maximum zigzag length found anywhere in the tree
        self.max_len = 0

        # DFS helper function: returns a tuple (left_len, right_len)
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                # Base case: A null node contributes nothing to the path length.
                return (-1, -1)

            # Recursively get the best zigzag paths from children
            left_result = dfs(node.left)
            right_result = dfs(node.right)

            # 1. Calculate the longest zigzag path ending at the current node by moving LEFT:
            # This path is the length of the previous *right* zigzag (from parent's left child) + 1.
            left_len = right_result[0] + 1

            # 2. Calculate the longest zigzag path ending at the current node by moving RIGHT:
            # This path is the length of the previous *left* zigzag (from parent's right child) + 1.
            right_len = left_result[1] + 1

            # 3. Update the global maximum length
            # The maximum length can be one of the paths we just calculated, 
            # or it could be one of the maximums found in the subtrees.
            self.max_len = max(self.max_len, left_len, right_len)
            
            # Return the best paths that can be extended by the parent of the current node
            return (left_len, right_len)

        dfs(root)
        return self.max_len
