from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, res = 0, float("-inf")
        for n in nums:
            currSum = max(currSum + n, n)
            res = max(currSum, res)
        return res