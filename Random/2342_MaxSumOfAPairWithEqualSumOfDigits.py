from collections import defaultdict
import heapq
from typing import List

def getSumDigits(s):
    res = 0
    for d in s:
        res += int(d)
    return res

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        sumToIndex = defaultdict(list)
        for i, n in enumerate(nums):
            sumDigits = getSumDigits(str(n))
            if sumToIndex[sumDigits]:
                currMax = sumToIndex[sumDigits][0] * -1
                res = max(res, n + currMax)
            
            heapq.heappush(sumToIndex[sumDigits], n*-1)
        return res