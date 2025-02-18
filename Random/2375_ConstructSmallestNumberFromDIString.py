class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [False] * (len(pattern) + 1)
        res = []

        def check(p, i):
            if not used[i]:
                used[i] = True
                res.append(i + 1)
                if build(p + 1):
                    return True
                used[i] = False
                res.pop()
            return False

        def build(p):
            if p == len(pattern) + 1:
                return True if len(res) == len(used) else False
            
            if p == 0:
                for i in range(0, len(used)):
                    if check(p, i):
                        return

            increasing = pattern[p - 1] == "I"
            lastPushed = res[-1]
            if increasing:
                for i in range(lastPushed, len(used)):
                    if check(p, i):
                        return True
            else:
                for i in range(0, lastPushed-1):
                    if check(p, i):
                        return True
            return False

        build(0)
        return "".join(map(str, res))