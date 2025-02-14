class ProductOfNumbers:

    def __init__(self):
        self.prefixProducts = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProducts = [1]
        else:
            self.prefixProducts.append(self.prefixProducts[-1] * num)

    def getProduct(self, k: int) -> int:
        startInterval = len(self.prefixProducts) - k
        if startInterval < 1:
            return 0
        return self.prefixProducts[-1] // self.prefixProducts[startInterval - 1]
