from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, currAmount):
            key = (i, currAmount)
            if key in memo:
                return memo[key]
            if i == len(coins) or currAmount > amount:
                return 0
            if currAmount == amount:
                return 1
            
            memo[key] = dfs(i, currAmount + coins[i]) + dfs(i+1, currAmount)
            return memo[key]
            
        return dfs(0, 0)