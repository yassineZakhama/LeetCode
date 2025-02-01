class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        impossible = set()
        def dfs(i1, i2, i3, n, m, lastTaken):
            key = (i1, i2, i3)
            if key in impossible:
                return False

            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2) and abs(n-m) <= 1

            if i1 < len(s1) and s1[i1] == s3[i3]:
                newN = n if lastTaken == 1 else n + 1
                if dfs(i1+1, i2, i3+1, newN, m, 1):
                    return True
            
            if i2 < len(s2) and s2[i2] == s3[i3]:
                newM = m if lastTaken == 2 else m + 1
                if dfs(i1, i2+1, i3+1, n, newM, 2):
                    return True

            impossible.add(key)            
            return False
                            
            
        return dfs(0, 0, 0, 0, 0, -1)
    