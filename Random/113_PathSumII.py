from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res, currPath = [], []
        
        def dfs(node, currSum):
            currSum += node.val
            if not node.left and not node.right:
                if currSum == targetSum:
                    res.append(currPath.copy() + [node.val])
                return
            
            currPath.append(node.val)
            if node.left:
                dfs(node.left, currSum)
            if node.right:
                dfs(node.right, currSum)
            currPath.pop()

        dfs(root, 0)
        return res
        