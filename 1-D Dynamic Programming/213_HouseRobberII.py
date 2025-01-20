from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def houseRobberOne(nums):
            maxWithoutLeft, currMax = 0, 0
            for n in nums:
                newMax = max(currMax, maxWithoutLeft + n)
                maxWithoutLeft = currMax
                currMax = newMax
            return currMax
        
        return max(houseRobberOne(nums[:len(nums)-1]), houseRobberOne(nums[1:]))