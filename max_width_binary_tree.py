# ==============================================
# Project: Maximum Width of Binary Tree
# Language: Python 3
# Description:
#   Given the root of a binary tree, return the maximum width.
#   The width of one level is the length between the leftmost
#   and rightmost non-null nodes (including nulls in between).
# ==============================================

from collections import deque
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxWidthBinaryTree:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # (node, index)

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]
            max_width = max(max_width, last_index - first_index + 1)

            for _ in range(level_length):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return max_width


if __name__ == "__main__":
    print("=============================================")
    print("        MAXIMUM WIDTH OF BINARY TREE")
    print("=============================================")

    # Create binary tree:
    #          1
    #        /   \
    #       3     2
    #      / \     \
    #     5   3     9
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    solver = MaxWidthBinaryTree()
    print("Maximum Width:", solver.widthOfBinaryTree(root))

    print("\nProgram completed successfully!")
