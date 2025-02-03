from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr, res, i = 1, 1, 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            elif nums[i] > nums[i-1]:
                while i < len(nums) and nums[i] > nums[i-1]:
                    curr += 1
                    i += 1
            elif nums[i] < nums[i-1]:
                while i < len(nums) and nums[i] < nums[i-1]:
                    curr += 1
                    i += 1
                
            res = max(res, curr)
            curr = 1

        return res
