from typing import List

def isSafe(r, c, board):
    row = r - 1
    while row >= 0:
        if board[row][c] == "Q":
            return False
        row -= 1
        
    row, col = r - 1, c - 1
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    row, col = r - 1, c + 1
    while row >= 0 and col < len(board):
        if board[row][col] == "Q":
            return False
        row -= 1
        col += 1
    return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if isSafe(i, j, board):
                    board[i][j] = "Q"
                    dfs(i+1)
                    board[i][j] = "."

        dfs(0)
        return res