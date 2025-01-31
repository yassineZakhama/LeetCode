from typing import List

def merge(leftArr, rightArr, arr):
    i, l, r = 0, 0, 0
    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] < rightArr[r]:
            arr[i] = leftArr[l]
            l += 1
        else:
            arr[i] = rightArr[r]
            r += 1
        i += 1

    while l != len(leftArr):
        arr[i] = leftArr[l]
        i += 1
        l += 1

    while r != len(rightArr):
        arr[i] = rightArr[r]
        i += 1
        r += 1

def mergeSort(arr):
    if len(arr) == 1:
        return
    
    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    mergeSort(leftArr)
    mergeSort(rightArr)
    merge(leftArr, rightArr, arr)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mergeSort(nums)
        return nums