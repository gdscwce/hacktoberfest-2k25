import collections

# Definition for a binary tree node (same as above)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView_BFS(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        queue = collections.deque([root])
        result = []

        while queue:
            level_length = len(queue)
            
            # Iterate over all nodes at the current level
            for i in range(level_length):
                node = queue.popleft()
                
                # We only care about the *last* node processed at this level
                # since it is the rightmost one in the Level Order Traversal.
                if i == level_length - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result
