from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        currSum, oddCount, evenCount = 0, 0, 0
        res = 0

        for n in arr:
            currSum += n
            if currSum % 2:
                res += 1 + evenCount
                oddCount += 1
            else:
                res += oddCount
                evenCount += 1

        return res % (10**9 + 7)
