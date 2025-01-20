from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxWithoutLeft, currMax = 0, 0
        for n in nums:
            newMax = max(currMax, maxWithoutLeft + n)
            maxWithoutLeft = currMax
            currMax = newMax
        return newMax