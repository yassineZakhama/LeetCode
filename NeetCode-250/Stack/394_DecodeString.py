class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        left, right = 0, 0
        while left < len(s):
            if s[right].isdigit():
                while s[right].isdigit():
                    right += 1
                stack.append(int(s[left:right]))
                right += 1
            elif s[right] == "]":
                string = stack.pop()
                count = stack.pop()
                addStrToStack(string * count, stack)
                right += 1
            else:
                while right < len(s) and s[right] != "[" and s[right] != "]" and not s[right].isdigit():
                    right += 1
                addStrToStack(s[left:right], stack)
            left = right
            
        return "".join(stack)

def addStrToStack(s, stack):
    if stack and isinstance(stack[-1], str):
        stack[-1] += s
    else:
        stack.append(s)