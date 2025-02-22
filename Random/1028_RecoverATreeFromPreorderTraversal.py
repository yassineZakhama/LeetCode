from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        while i < len(traversal) and traversal[i].isdigit():
            i += 1
        root = TreeNode(int(traversal[:i]))

        stack = [root]
        while i < len(traversal):
            depth = 0
            while traversal[i] == "-":
                depth += 1
                i += 1
            
            endNumber = i + 1
            while endNumber < len(traversal) and traversal[endNumber].isdigit():
                endNumber += 1
            newNode = TreeNode(int(traversal[i:endNumber]))
            
            if depth == len(stack):
                stack[-1].left = newNode
            else:
                while depth != len(stack):
                    stack.pop()
                stack[-1].right = newNode
            stack.append(newNode)
            i = endNumber
        return root
