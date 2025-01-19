from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i not in memo:
                memo[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return memo[i]

        return max(dfs(0), dfs(1))

class Solution2: # O(1) space
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        if len(nums) > 2:
            nums[len(nums)-3] += nums[-1]

        for i in range(len(nums)-4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])
        
        return max(nums[0], nums[1])