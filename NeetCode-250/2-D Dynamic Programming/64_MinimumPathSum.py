from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {(rows-1, cols-1): grid[rows-1][cols-1]}

        def dfs(i, j): 
            key = (i, j)
            if key in memo:
                return memo[key]

            if i == rows or j == cols:
                return float("inf")

            down = grid[i][j] + dfs(i+1, j)
            right = grid[i][j] + dfs(i, j+1)

            memo[key] = min(down, right)
            return memo[key]

        return dfs(0, 0)