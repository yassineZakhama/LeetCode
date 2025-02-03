from collections import deque
from typing import List

graph = {
    0: [1, 9],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 0]
    }

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = [0, 0, 0, 0]
        
        q = deque()
        q.append(start)
        res = 0
        while q:
            lvl = len(q)
            while lvl:
                lvl -= 1
                candidateArr = q.popleft()
                candidate = "".join(map(str, candidateArr))
                if candidate == target:
                    return res
                if candidate in deadends:
                    continue
                deadends.add(candidate)
                for i in range(4):
                    copy1 = candidateArr.copy()
                    copy2 = candidateArr.copy()
                    copy1[i] = graph[copy1[i]][0]
                    copy2[i] = graph[copy2[i]][1]
                    q.append(copy1)
                    q.append(copy2)

            res += 1
        
        return -1
