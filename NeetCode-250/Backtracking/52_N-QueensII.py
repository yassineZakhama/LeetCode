class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, negDiag, posDiag = set(), set(), set()
        res = [0]

        def backtrack(r):
            if r == n:
                res[0] += 1
                return

            for c in range(n):
                neg, pos = r - c, r + c
                if c not in cols and neg not in negDiag and pos not in posDiag:
                    cols.add(c)
                    negDiag.add(neg)
                    posDiag.add(pos)

                    backtrack(r+1)
                    
                    cols.remove(c)
                    negDiag.remove(neg)
                    posDiag.remove(pos)

        backtrack(0)
        return res[0]