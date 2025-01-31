from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, climbing, prevHeight):
            key = (i, j)
            if i < 0 or j < 0 or i == rows or j == cols or key in climbing or heights[i][j] < prevHeight:
                return False
            climbing.add(key)
            dfs(i+1, j, climbing, heights[i][j])
            dfs(i, j+1, climbing, heights[i][j])
            dfs(i-1, j, climbing, heights[i][j])
            dfs(i, j-1, climbing, heights[i][j])
            
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                key = (r,c)
                if key in pacific and key in atlantic:
                    res.append([r,c]) 
        
        return res