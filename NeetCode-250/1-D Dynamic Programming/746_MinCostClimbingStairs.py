from typing import List

class Solution: # Top-Down
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i not in memo:
                memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i] 

        return min(dfs(0), dfs(1))

class Solution2: # Top-Down; O(1) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])