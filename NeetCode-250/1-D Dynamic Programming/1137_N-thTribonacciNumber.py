memo = {
    0: 0,
    1: 1,
    2: 1
}

class Solution: # Top-Down
    def tribonacci(self, n: int) -> int:
        if n not in memo:
            memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return memo[n]
    

class Solution2: # Bottom-Up; O(1) space
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        
        for _ in range(3, n):
            new = sum(t)
            t[0] = t[1]
            t[1] = t[2]
            t[2] = new
        return sum(t)