from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for left1 in range(0, len(nums)):
            if left1 > 0 and nums[left1] == nums[left1 - 1]:
                continue
            
            for right1 in range(left1 + 1, len(nums)):
                if right1 > left1 + 1 and nums[right1] == nums[right1 - 1]:
                    continue
                
                left2, right2 = right1 + 1, len(nums) - 1

                while left2 < right2:
                    total = nums[left1] + nums[right1] + nums[left2] + nums[right2]
                    if total == target:
                        res.append([nums[left1], nums[right1], nums[left2], nums[right2]])
                        left2 += 1
                        right2 -= 1
                        while left2 < right2 and nums[left2 - 1] == nums[left2]:
                            left2 += 1
                        while left2 < right2 and nums[right2 + 1] == nums[right2]:
                            right2 -= 1
                    elif total < target:
                        left2 += 1
                    else:
                        right2 -= 1

        return res
