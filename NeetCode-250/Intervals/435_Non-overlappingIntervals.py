from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        previous = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if previous[1] > current[0]:
                res += 1
                if current[1] < previous[1]:
                    previous = current
            else:
                previous = current
        return res