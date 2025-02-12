import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        remaining = [0] * 26
        for task in tasks:
            i = ord(task) - ord("A")
            remaining[i] += 1
        
        heap = [] # time to task index  
        for i in range(len(remaining)):
            if remaining[i]:
                heap.append([0, i])
        heapq.heapify(heap)

        time = 0
        while heap:
            if heap[0][0] <= time:
                t, i = heapq.heappop(heap)
                remaining[i] -= 1
                if remaining[i]:
                    heapq.heappush(heap, [t+n+1, i])
            time += 1
        return time