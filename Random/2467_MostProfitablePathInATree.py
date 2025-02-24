from collections import defaultdict
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        bobTimes = {bob: 0}
        def calculateBobTimes(n, parent, time):
            for nei in adj[n]:
                if nei == parent:
                    continue

                bobTimes[nei] = time
                if nei == 0:
                    return True

                if calculateBobTimes(nei, n, time + 1):
                    return True
                del bobTimes[nei]
        calculateBobTimes(bob, -1, 1)
        
        res = [float("-inf")]
        def dfs(n, parent, time, currProfit):
            if n not in bobTimes or n in bobTimes and time < bobTimes[n]:
                currProfit += amount[n]
            elif n in bobTimes and time == bobTimes[n]:
                currProfit += amount[n] // 2
        
            if len(adj[n]) == 1 and adj[n][0] == parent:
                res[0] = max(res[0], currProfit)
                return

            for nei in adj[n]:
                if nei == parent:
                    continue
                dfs(nei, n, time + 1, currProfit)  

        dfs(0, -1, 0, 0)
        return res[0]
    