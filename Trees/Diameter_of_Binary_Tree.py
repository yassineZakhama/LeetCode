from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(node): 
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            res[0] = max(res[0], leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return res[0]