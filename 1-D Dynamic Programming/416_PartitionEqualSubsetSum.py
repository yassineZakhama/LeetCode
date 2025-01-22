from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums)
        if arrSum % 2 != 0:
            return False

        TARGET = arrSum // 2
        memo = {}
        
        def dfs(i, currSum):
            if currSum > TARGET or i >= len(nums):
                return False
            
            key = (i, currSum) 
            if key in memo:
                return memo[key]            
            if currSum == TARGET:
                return True
            
            memo[key] = dfs(i+1, currSum  + nums[i]) or dfs(i+1, currSum)
            return memo[key] 

        return dfs(0, 0)