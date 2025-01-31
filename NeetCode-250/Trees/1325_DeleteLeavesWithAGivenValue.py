from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(n):
            if not n.left and not n.right:
                return True if n.val == target else False
            
            if n.left and dfs(n.left):
                n.left = None
            if n.right and dfs(n.right):
                n.right = None
            
            if not n.left and not n.right and n.val == target:
                return True
            return False
        
        return None if dfs(root) else root