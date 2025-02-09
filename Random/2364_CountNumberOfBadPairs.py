from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        possiblePairs, goodPairs = n*(n-1)//2, 0
        m = {}
        for i in range(n):
            diff = nums[i] - i
            m[diff] = m.get(diff, 0) + 1
            goodPairs += m[diff] - 1
        
        return possiblePairs - goodPairs