from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odds = set()
        for n in nums:
            if n not in odds:
                odds.add(n)
            else:
                odds.remove(n)
        return len(odds) == 0