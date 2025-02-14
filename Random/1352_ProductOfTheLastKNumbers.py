class ProductOfNumbers:

    def __init__(self):
        self.lastZero = -1
        self.product = []

    def add(self, num: int) -> None:
        if num == 0:
            self.lastZero = len(self.product)
            self.product.append(0)
        elif not self.product or self.product[-1] == 0:
            self.product.append(num)
        else:
            self.product.append(num * self.product[-1])

    def getProduct(self, k: int) -> int:
        startInterval = len(self.product) - k
        if startInterval == 0:
            return self.product[-1] if self.lastZero == -1 else 0

        if self.lastZero >= startInterval:
            return 0

        if self.product[startInterval - 1] != 0:
            return self.product[-1] // self.product[startInterval - 1]
        else:
            return self.product[-1]