from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.populate(root)

    def next(self) -> int:
        top = self.stack.pop()
        self.populate(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def populate(self, n):
        while n:
            self.stack.append(n)
            n = n.left