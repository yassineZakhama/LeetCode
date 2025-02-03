from collections import deque
from typing import List

graph = {
    "0": ["1", "9"],
    "1": ["0", "2"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["3", "5"],
    "5": ["4", "6"],
    "6": ["5", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "0"]
}

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        q = deque()
        q.append("0000")
        res = 0
        while q:
            lvl = len(q)
            while lvl:
                lvl -= 1
                candidate = q.popleft()
                if candidate == target:
                    return res
                if candidate in deadends:
                    continue
                deadends.add(candidate)
                for i in range(4):
                    n = candidate[i]
                    q.append(candidate[:i] + graph[n][0] + candidate[i+1:])
                    q.append(candidate[:i] + graph[n][1] + candidate[i+1:])

            res += 1
        
        return -1
