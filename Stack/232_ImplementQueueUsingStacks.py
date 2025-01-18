class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp = []
        self.top = 0

    def push(self, x: int) -> None:
        if not len(self.stack):
            self.top = x
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 1:
            return self.stack.pop()
        
        while len(self.stack) != 1:
            self.temp.append(self.stack.pop())
        self.top = self.temp[-1]
        res = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return res

    def peek(self) -> int:
        return self.top

    def empty(self) -> bool:
        return len(self.stack) == 0
