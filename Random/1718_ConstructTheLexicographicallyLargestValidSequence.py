from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (n * 2 - 1)
        used = set()

        def construct(i):
            if i == len(res):
                return True

            for num in range(n, 0, -1):
                if num in used:
                    continue
                if num > 1 and (i + num >= len(res) or res[i + num]):
                    continue

                used.add(num)

                res[i] = num
                if num > 1:
                    res[i + num] = num
                
                j = i + 1
                while j < len(res) and res[j]:
                    j += 1
                if construct(j):
                    return True

                res[i] = 0
                if num > 1:
                    res[i + num] = 0

                used.remove(num)

        construct(0)
        return res
