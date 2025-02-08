from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.numberToIndices = defaultdict(list)
        self.indexToNumber = {}

    def change(self, index: int, number: int) -> None:
        self.indexToNumber[index] = number
        heapq.heappush(self.numberToIndices[number], index)

    def find(self, number: int) -> int:
        while self.numberToIndices[number]:
            currMin = self.numberToIndices[number][0]
            if number == self.indexToNumber[currMin]:
                return currMin
            heapq.heappop(self.numberToIndices[number])

        return -1