# ==============================================
# Project: Binary Tree Right Side View
# Language: Python 3
# Description:
#   Given the root of a binary tree, return the values of the nodes
#   you can see ordered from top to bottom from the right side.
# ==============================================

from collections import deque
from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeRightView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        view = []
        queue = deque([root])

        # Level-order traversal (BFS)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # last node of this level → visible from right side
                if i == level_size - 1:
                    view.append(node.val)
        return view


if __name__ == "__main__":
    print("=============================================")
    print("        BINARY TREE RIGHT SIDE VIEW")
    print("=============================================")

    # Create binary tree:
    #        1
    #      /   \
    #     2     3
    #      \     \
    #       5     4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    solver = BinaryTreeRightView()
    print("Right Side View:", solver.rightSideView(root))

    print("\nProgram completed successfully!")
