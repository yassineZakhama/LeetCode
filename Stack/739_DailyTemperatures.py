from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # monotonic decreasing stack; stores (index, temperature) tuples

        for idx, tpr in enumerate(temperatures):
            while stack and stack[-1][1] < tpr:
                idxTop, _ = stack.pop() 
                res[idxTop] = idx - idxTop
            
            stack.append((idx, tpr))

        return res