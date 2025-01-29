from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def match(s1, i2):
            differ = False
            s2 = wordList[i2]
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if differ:
                        return 
                    differ = True
            adj[s1].add(s2)
            adj[s2].add(s1)
            

        adj = defaultdict(set)
        for i in range(len(wordList)):
            s = wordList[i]
            match(beginWord, i)
            for j in range(i+1, len(wordList)):
                match(s, j)

        vis = set()
        res = 0
        queue = deque()
        queue.append(beginWord)
        while queue:
            res += 1
            lvl = len(queue)
            while lvl:
                lvl -= 1
                v = queue.popleft()
                if v == endWord:
                    return res
                if v not in vis:
                    vis.add(v)
                    for u in adj[v]:
                        queue.append(u)
        return 0