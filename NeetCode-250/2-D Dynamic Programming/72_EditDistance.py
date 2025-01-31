class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]

            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j

            if word1[i] == word2[j]:
                memo[key] = dfs(i+1, j+1)
            else:
                memo[key] = 1 + min(dfs(i, j+1), dfs(i+1, j+1), dfs(i+1, j)) 
            return memo[key]
        
        return dfs(0, 0)