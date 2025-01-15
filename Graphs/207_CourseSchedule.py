from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)
        
        visited, visiting = set(), set()

        def dfs(v):
            if v in visiting:
                return True
            if v in visited:
                return False
            
            visited.add(v)
            
            visiting.add(v)
            for neighbor in pre[v]:
                if dfs(neighbor):
                    return True     
            visiting.remove(v)

            return False


        for v in range(numCourses):
            if v in pre and v not in visited:
                if dfs(v):
                    return False
        return True