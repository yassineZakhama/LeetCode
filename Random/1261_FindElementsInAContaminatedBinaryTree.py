
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        if root:
            root.val = 0
            self.recover(root)        

    def find(self, target: int) -> bool:
        return target in self.values

    def recover(self, root):
        self.values.add(root.val)
        if root.left:
            root.left.val = root.val * 2 + 1
            self.recover(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.recover(root.right)