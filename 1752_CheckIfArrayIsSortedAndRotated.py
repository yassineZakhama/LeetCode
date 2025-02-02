from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if nums[n-1] > nums[0]:
            for i in range(1, n):
                if nums[i] < nums[i-1]:
                    return False
        else:
            joker = True
            for i in range(1, n):
                if nums[i] < nums[i-1]:
                    if not joker:
                        return False
                    joker = False
        return True

# Circular comparison
class Solution2:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  
                count += 1
                if count > 1:
                    return False
                
        return True