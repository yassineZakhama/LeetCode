from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        productToCount = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p = nums[i] * nums[j]
                count = productToCount.get(p, 0)
                if count > 0:
                    res += 8 * count
                productToCount[p] = count + 1
        return res