class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1

            if i in memo:
                return memo[i]
            
            res = 0

            if s[i] != "0":
                res += dfs(i+1)

            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)

            memo[i] = res
            return res
        
        return dfs(0)
        
