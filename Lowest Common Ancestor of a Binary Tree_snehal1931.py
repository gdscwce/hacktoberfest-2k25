from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Base Case 1: If we reach a null node, return None.
        # Base Case 2: If the current node is one of the targets (p or q), 
        # return the node itself. This handles cases where one node is an ancestor of the other.
        if not root or root == p or root == q:
            return root

        # Recursively search the left and right subtrees
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        # Decision Logic (While backtracking):
        
        # Case 1: If both left and right return a non-null node, 
        # it means p was found in one subtree and q was found in the other.
        # The current 'root' is the LCA.
        if left_result and right_result:
            return root
        
        # Case 2: If only one side returns a non-null node (left_result or right_result),
        # this means both p and q must be in that one subtree (or one node was found, 
        # and we continue propagating it up). We return that non-null result.
        # This is concisely handled by 'left_result or right_result'.
        else:
            return left_result or right_result
