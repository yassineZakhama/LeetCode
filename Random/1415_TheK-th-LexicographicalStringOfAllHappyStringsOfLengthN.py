class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ["a", "b", "c"]
        achieved, res = [0], []

        def backtrack():
            if len(res) == n:
                achieved[0] += 1
                return achieved[0] == k

            if not res:
                for c in chars:
                    res.append(c)
                    if backtrack():
                        return True
                    res.pop()
            else:
                for c in chars:
                    if c == res[-1]:
                        continue
                    res.append(c)
                    if backtrack():
                        return True
                    res.pop()

            return False

        return "".join(res) if backtrack() else ""