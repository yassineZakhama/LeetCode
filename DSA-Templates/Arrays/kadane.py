# Find the maximum sum subarray in an array of numbers
def kadane(nums):
    maxSum = float('-inf')
    currentSum = 0

    for num in nums:
        currentSum = max(num, currentSum + num)  # Choose to extend or start fresh
        maxSum = max(maxSum, currentSum)

    return maxSum
