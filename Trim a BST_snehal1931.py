class TreeNode:
    # ... (same as above)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
        Recursively trims the BST to contain only nodes with values in the range [low, high].
        """
        if not root:
            return None

        # If root.val is too small, the new root must be in the right subtree
        # (since all nodes in the left subtree will also be too small).
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If root.val is too large, the new root must be in the left subtree
        # (since all nodes in the right subtree will also be too large).
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # If root.val is within the range, trim its children.
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
