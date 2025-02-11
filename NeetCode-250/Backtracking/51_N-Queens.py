from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols, negDiag, posDiag = set(), set(), set()
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                neg, pos = r - c, r + c
                if c not in cols and neg not in negDiag and pos not in posDiag:
                    cols.add(c)
                    negDiag.add(neg)
                    posDiag.add(pos)
                    board[r][c] = "Q"

                    backtrack(r+1)
                    
                    board[r][c] = "."
                    cols.remove(c)
                    negDiag.remove(neg)
                    posDiag.remove(pos)

        backtrack(0)
        return res