# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        Checks if the root's value equals the sum of its two children's values.
        The problem guarantees the tree has exactly 3 nodes.
        """
        # The boolean expression directly returns True or False based on the comparison.
        return root.val == root.left.val + root.right.val
