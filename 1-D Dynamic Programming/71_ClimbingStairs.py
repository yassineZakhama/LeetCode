memo = {
    1: 1,
    2: 2
}

class Solution: # Top-Down
    def climbStairs(self, n: int) -> int:
        if n not in memo:
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]

class Solution2: # Bottom-Up; O(1) space
    def climbStairs(self, n: int) -> int:
        s = [1, 2]

        if n <= 2:
            return s[n-1]
        
        for _ in range(3, n):
            new = s[0] + s[1]
            s[0] = s[1]
            s[1] = new
        return s[0] + s[1]