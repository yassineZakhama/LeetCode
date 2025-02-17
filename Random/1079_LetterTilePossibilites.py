class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = {}
        for c in tiles:
            count[c] = count.get(c, 0) + 1

        def backtrack():
            res = 0
            for c in count:
                if count[c]:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1
            return res

        return backtrack()
