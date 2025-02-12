from typing import List

def getSumDigits(s):
    res = 0
    for d in s:
        res += int(d)
    return res

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        sumToNumber = {}
        for n in nums:
            sumDigits = getSumDigits(str(n))
            if sumDigits in sumToNumber:
                currMax = sumToNumber[sumDigits]
                res = max(res, n + currMax)
                sumToNumber[sumDigits] = max(currMax, n)
            else:
                sumToNumber[sumDigits] = n

        return res