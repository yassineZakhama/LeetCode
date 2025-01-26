from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, bought):
            key = (i, bought)
            if key in memo:
                return memo[key]

            if i >= len(prices):
                return 0

            profit = 0

            if bought:
                sell = dfs(i+2, False) + prices[i]
                skip = dfs(i+1, bought) 
                profit = max(sell, skip)
            else:
                buy = dfs(i+1, True) - prices[i] 
                skip = dfs(i+1, bought) 
                profit = max(buy, skip)
            
            memo[key] = profit
            return profit 

        return dfs(0, False)