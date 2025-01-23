from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][cols-1]:
                row = matrix[i]
                left, right = 0, cols - 1

                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1 
                                        
                return False

        return False