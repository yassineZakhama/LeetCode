from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        vis, heap = set(), [(0, k)]
        dist = [float("inf")] * (n + 1)
        dist[0], dist[k] = 0, 0

        while heap:
            d, u = heapq.heappop(heap)
            for v, w in adj[u]:
                candidateNewDist = d + w
                if v not in vis and candidateNewDist < dist[v]:
                    dist[v] = candidateNewDist
                    heapq.heappush(heap, (candidateNewDist, v))
            vis.add(u)

        res = max(dist)
        return res if res != float("inf") else -1