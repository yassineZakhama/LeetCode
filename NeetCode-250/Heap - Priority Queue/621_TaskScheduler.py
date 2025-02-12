from collections import deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            i = ord(task) - ord("A")
            count[i] += 1
        
        heap, q = [], deque()
        for i in range(len(count)):
            if count[i]:
                heap.append(-count[i])
        heapq.heapify(heap)

        time = 0
        while heap or q:
            if heap:
                c = heapq.heappop(heap)
                if c + 1 != 0:
                    q.append((c+1, time+n))
            if q and q[0][1] == time:
                c, _ = q.popleft()
                heapq.heappush(heap, c)
            time += 1
        return time
