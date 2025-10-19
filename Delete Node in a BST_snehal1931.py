class TreeNode:
    # ... (same as above)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # Found the node to delete
            # Case 1 & 2: Node has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: Node has 2 children
            # Find the smallest node in the right subtree (in-order successor)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace the current node's value with the successor's value
            root.val = successor.val
            
            # Delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root
