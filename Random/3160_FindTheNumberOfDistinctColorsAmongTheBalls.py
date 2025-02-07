from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        colorToBalls, ballToColor = defaultdict(set), {}

        for i in range(len(queries)):
            ball, color = queries[i]

            currColor = ballToColor.get(ball, 0)
            if currColor == 0:
                ballToColor[ball] = color
                colorToBalls[color].add(ball)
            else:
                if len(colorToBalls[currColor]) == 1:
                    del colorToBalls[currColor]
                else:
                    colorToBalls[currColor].remove(ball)
                ballToColor[ball] = color
                colorToBalls[color].add(ball)

            res[i] = len(colorToBalls)                

        return res