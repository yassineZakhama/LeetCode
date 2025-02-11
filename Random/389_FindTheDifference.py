class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            i = ord(c) - ord('a')
            count[i] -= 1
            if count[i] < 0:
                return c