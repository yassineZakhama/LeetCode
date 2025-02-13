import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        steps = 0
        heapq.heapify(nums)
        while len(nums) > 1 and nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            res = min(first, second) * 2 + max(first, second)
            heapq.heappush(nums, res)
            steps += 1
        return steps