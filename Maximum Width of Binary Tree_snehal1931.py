import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        # Queue stores tuples of (node, index)
        # We start the root at index 1 (or 0, but 1 is conventional for 2*i, 2*i+1)
        queue = collections.deque([(root, 1)])
        max_width = 0

        while queue:
            level_length = len(queue)
            
            # The index of the leftmost node at the current level
            level_start_index = queue[0][1] 
            
            # The indices of the rightmost and leftmost nodes at this level
            leftmost_index = 0
            rightmost_index = 0

            # Process all nodes at the current level
            for i in range(level_length):
                node, original_index = queue.popleft()
                
                # Normalize the index to prevent integer overflow.
                # 'normalized_index' will be small (starts at 0)
                normalized_index = original_index - level_start_index
                
                # Record the indices of the first (leftmost) and last (rightmost) node
                if i == 0:
                    leftmost_index = normalized_index
                if i == level_length - 1:
                    rightmost_index = normalized_index

                # Add children to the queue for the next level, using the 2*i, 2*i+1 rule.
                # We apply the rule to the *original* index to maintain correct relative spacing
                # for the next level, but we will normalize them again later.
                if node.left:
                    # Index of left child: 2 * original_index
                    queue.append((node.left, 2 * original_index))
                if node.right:
                    # Index of right child: 2 * original_index + 1
                    queue.append((node.right, 2 * original_index + 1))
            
            # Calculate the width of the current level
            current_width = rightmost_index - leftmost_index + 1
            max_width = max(max_width, current_width)

        return max_width
