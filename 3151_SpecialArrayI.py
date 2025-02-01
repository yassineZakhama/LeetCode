from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isPreviousEven = True if nums[0] % 2 == 0 else False
        for i in range(1, len(nums)):
            isCurrentEven = nums[i] % 2 == 0
            if isPreviousEven == isCurrentEven:
                return False
            isPreviousEven = isCurrentEven
        
        return True