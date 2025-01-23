from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0

        memo = {}

        def dfs(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]
            
            if i == rows - 1 and j == cols - 1:
                return 1
            if i == rows or j == cols or obstacleGrid[i][j] == 1:
                return 0
            
            memo[key] = dfs(i+1, j) + dfs(i, j+1)
            return memo[key]
            
        return dfs(0,0)
            
            