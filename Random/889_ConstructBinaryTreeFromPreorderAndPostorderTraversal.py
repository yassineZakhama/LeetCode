from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        startRightSubTreeInPreorder = preorder.index(postorder[-2])

        left = self.constructFromPrePost(preorder[1:startRightSubTreeInPreorder], 
                postorder[:startRightSubTreeInPreorder - 1])
        right = self.constructFromPrePost(preorder[startRightSubTreeInPreorder:], 
                postorder[startRightSubTreeInPreorder - 1 : len(postorder) - 1])
        
        return TreeNode(preorder[0], left, right)