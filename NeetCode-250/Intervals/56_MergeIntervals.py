from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            previous = res[-1]
            if previous[1] >= interval[0]:
                previous[1] = max(previous[1], interval[1])
            else:
                res.append(interval)
        return res
