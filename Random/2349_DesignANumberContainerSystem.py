from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.numberToIndices = defaultdict(SortedSet)
        self.indexToNumber = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber:
            oldNumber = self.indexToNumber[index]
            self.numberToIndices[oldNumber].remove(index)

        self.indexToNumber[index] = number
        self.numberToIndices[number].add(index)

    def find(self, number: int) -> int:
        return self.numberToIndices[number][0] if self.numberToIndices[number] else -1
