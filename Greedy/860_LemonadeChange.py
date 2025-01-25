from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0

        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if not fives:
                    return False
                tens += 1
                fives -= 1
            else:
                if not fives:
                    return False
                elif not tens:
                    if fives < 3:
                        return False
                    fives -= 3
                else:
                    fives -= 1
                    tens -= 1
        return True