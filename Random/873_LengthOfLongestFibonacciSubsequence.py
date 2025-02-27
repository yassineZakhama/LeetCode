from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)

        longest = 0
        for i in range(len(arr)):
            first = arr[i]
            for j in range(i+1, len(arr)):
                second = arr[j]
                matches = 2
                candidateSum = first + second
                if candidateSum in nums:
                    while candidateSum in nums:
                        matches += 1
                        first = second
                        second = candidateSum
                        candidateSum = first + second
                    longest = max(matches, longest)
                    first = arr[i]

        return longest if longest > 2 else 0
