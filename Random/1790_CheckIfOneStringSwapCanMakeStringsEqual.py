class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differences = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if len(differences) == 2:
                    return False
                differences.append(i)
        
        return (not differences or len(differences) == 2 
            and s1[differences[0]] == s2[differences[1]] and s2[differences[0]] == s1[differences[1]])