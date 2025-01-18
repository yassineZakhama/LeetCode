from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def build(nbrOpening, nbrClosing):
            if nbrOpening == nbrClosing == n:
                res.append("".join(stack))
                return
            
            if nbrOpening < n:
                stack.append("(")
                build(nbrOpening + 1, nbrClosing)
                stack.pop()
            
            if nbrClosing < nbrOpening:
                stack.append(")")
                build(nbrOpening, nbrClosing + 1)
                stack.pop()

        build(0, 0)
        return res
