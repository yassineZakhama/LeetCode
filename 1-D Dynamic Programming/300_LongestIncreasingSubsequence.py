from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if memo[i] != 1:
                return memo[i]

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    memo[i] = max(memo[i], 1 + dfs(j))
            
            return memo[i]
        
        for i in range(len(nums)):
            dfs(i)
        return max(memo)