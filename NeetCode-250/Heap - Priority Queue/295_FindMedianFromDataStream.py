def findInsertPosition(nums, n):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return left

class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        i = findInsertPosition(self.data, num)
        self.data = self.data[:i] + [num] + self.data[i:]

    def findMedian(self) -> float:
        i = len(self.data) // 2
        if len(self.data) % 2 == 0:
            return (self.data[i] + self.data[i-1]) / 2
        else:
            return self.data[i]
