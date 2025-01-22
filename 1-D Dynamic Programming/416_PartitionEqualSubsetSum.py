from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums)
        if arrSum % 2 != 0:
            return False

        memo = {}

        def dfs(i, currSum, target):
            if currSum > target or i >= len(nums):
                return False
            
            key = (i, currSum) 
            if key in memo:
                return memo[key]            
            if currSum == target:
                return True
            
            memo[key] = dfs(i+1, currSum  + nums[i], target) or dfs(i+1, currSum, target)
            return memo[key] 

        return dfs(0, 0, arrSum / 2)