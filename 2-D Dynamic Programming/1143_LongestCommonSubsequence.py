class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]

            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                memo[key] = 1 + dfs(i+1, j+1)
                return memo[key]

            memo[key] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[key]
            
        return dfs(0, 0)
