from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums)
        if arrSum % 2 != 0:
            return False
        target = arrSum // 2

        memo = {}

        def dfs(i, currSum):
            nonlocal target

            if i >= len(nums):
                return False
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            if currSum == target:
                return True
            if currSum > target:
                return False
            
            if dfs(i+1, currSum  + nums[i]) or dfs(i+1, currSum):
                return True

            memo[(i, currSum)] = False
            return False
        return dfs(0, 0)