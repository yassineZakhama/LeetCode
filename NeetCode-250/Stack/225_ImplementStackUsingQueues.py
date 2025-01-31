from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()
        self.t = 0

    def push(self, x: int) -> None:
        self.t = x
        self.q.append(x)

    def pop(self) -> int:
        l = len(self.q)
        while l != 1:
            self.t = self.q[0]
            self.q.append(self.q.popleft())
            l -= 1
        return self.q.popleft()

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.q) == 0        
