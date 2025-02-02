from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        temp, res = [], []
        
        def pushIfValid():
            if len(temp) != 4:
                return
            for candidate in temp:
                if not (candidate == "0" or candidate[0] != "0" and int(candidate) <= 255): 
                    return
            res.append(".".join(temp))

        def dfs(i):
            if i == len(s):
                pushIfValid()
                return

            for j in range(i, i+4):
                if j >= len(s):
                    break
                
                temp.append(s[i:j+1])
                dfs(j+1)
                temp.pop()

        dfs(0)
        return res
