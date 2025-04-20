from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        found = {}
        n = 0

        for ans in answers:
            if ans == 0:
                n += 1
                continue 
            
            if ans not in found:
                n += ans + 1
                found[ans] = ans
                continue

            found[ans] -= 1
            if found[ans] == 0:
                del found[ans]
        
        return n