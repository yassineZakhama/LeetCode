class StockSpanner:
    def __init__(self):
        self.prices = []
        self.stack = [] # (p, i) tuples        

    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices) - 1

        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, i))
            return 1
        
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop() 
        res = i + 1 if not self.stack else i - self.stack[-1][1]
        self.stack.append((price, i))
        return res 
        