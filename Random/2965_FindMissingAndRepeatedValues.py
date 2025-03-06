from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = len(grid[0]) * len(grid[0])
        nums = set([i for i in range(1, values + 1)])

        repeating = 0
        for g in grid:
            for n in g:
                if n not in nums:
                    repeating = n
                else:
                    nums.remove(n)
        return [repeating, list(nums)[0]]