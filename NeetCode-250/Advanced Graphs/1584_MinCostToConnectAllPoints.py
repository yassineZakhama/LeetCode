from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                w = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((w, j))
                adj[j].append((w, i))
        

        heap, vis, res = [(0, 0)], set(), 0

        while heap:
            w1, u = heapq.heappop(heap)
            if u in vis:
                continue
            
            vis.add(u)
            res += w1
            for w2, v in adj[u]:
                if v not in vis:
                    heapq.heappush(heap, (w2, v))

        return res