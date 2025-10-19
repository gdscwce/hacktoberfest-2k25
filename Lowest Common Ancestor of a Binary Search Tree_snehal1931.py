class TreeNode:
    # ... (same as above)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the LCA of two nodes in a BST using the BST property.
        """
        curr = root
        while curr:
            # If both p and q are greater than the current node, search the right subtree.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are smaller than the current node, search the left subtree.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Otherwise, the current node is the LCA (split point or p/q itself).
            else:
                return curr
