from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "+":
                stack.append(stack.pop() + stack.pop()) 
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]