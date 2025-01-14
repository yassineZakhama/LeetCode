from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)
        
        q = deque()
        visited, visiting = set(), set()

        def dfs(v):
            if v in visiting:
                return True # Back edge detected 
            if v in visited:
                return False
            
            visited.add(v)
            visiting.add(v)
            
            for neighbor in pre[v]:
                if dfs(neighbor):
                    return True
            
            visiting.remove(v)
            q.append(v)
            return False

        for v in range(numCourses):
            if v not in visited:
                if dfs(v):
                    return []
        
        ordering = []
        while q:
            ordering.append(q.popleft())
        return ordering
    