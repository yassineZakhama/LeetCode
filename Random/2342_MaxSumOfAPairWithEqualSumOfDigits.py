from typing import List

def getSumDigits(n):
    res = 0
    while n > 0:
        res += n % 10 
        n //= 10 
    return res

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        sumToNumber = {}
        for n in nums:
            sumDigits = getSumDigits(n)
            if sumDigits in sumToNumber:
                currMax = sumToNumber[sumDigits]
                res = max(res, n + currMax)
                sumToNumber[sumDigits] = max(currMax, n)
            else:
                sumToNumber[sumDigits] = n

        return res