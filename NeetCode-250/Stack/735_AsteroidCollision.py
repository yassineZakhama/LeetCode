from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            a = asteroids[i]
            if a >= 0 or not len(stack) or stack[-1] < 0:
                stack.append(a)
                i += 1
                continue

            top = stack[-1]
            if abs(top) == abs(a):
                stack.pop()
                i += 1
            elif abs(top) < abs(a):
                stack.pop()
            else:
                i += 1

        return stack
