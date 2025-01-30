from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node, canTake):
            key = (node, canTake)
            if key in memo:
                return memo[key]
            if not node:
                return 0
            
            if canTake:
                take = node.val + dfs(node.left, False) + dfs(node.right, False)
                skip = dfs(node.left, True) + dfs(node.right, True)
                memo[key] = max(take, skip) 
                return memo[key] 
            else:
                return dfs(node.left, True) + dfs(node.right, True)
        
        return dfs(root, True)