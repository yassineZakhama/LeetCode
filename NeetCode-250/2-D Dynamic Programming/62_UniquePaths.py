memo = {}

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        key = (m, n)
        if key in memo:
            return memo[key]

        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        
        memo[key] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return memo[key]