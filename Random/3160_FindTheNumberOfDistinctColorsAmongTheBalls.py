from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorToBalls, ballToColor = defaultdict(set), {}
        res = []

        for ball, color in queries:
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

            res.append(len(colorToBalls))                

        return res