from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # Hash map to store the frequency of cumulative sums encountered
        # {prefix_sum: frequency}. Initialize with {0: 1} for the empty path.
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        # Use a list to hold the count, allowing the inner function to modify it
        # (or use a class instance variable).
        self.count = 0
        
        def dfs(node: Optional[TreeNode], current_sum: int) -> None:
            if not node:
                return

            # 1. Update current running sum
            current_sum += node.val

            # 2. Check for valid paths ending at the current node
            # A valid path exists if an earlier sum (current_sum - targetSum) was recorded.
            required_sum = current_sum - targetSum
            self.count += prefix_sums[required_sum]
            
            # 3. Add the current sum to the hash map for future nodes to reference
            prefix_sums[current_sum] += 1
            
            # 4. Recurse
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            # 5. Backtrack: Remove the current sum's contribution before returning
            # This is essential to prevent sibling/cousin paths from using this prefix sum.
            prefix_sums[current_sum] -= 1
            if prefix_sums[current_sum] == 0:
                del prefix_sums[current_sum] # Optional optimization

        dfs(root, 0)
        return self.count
