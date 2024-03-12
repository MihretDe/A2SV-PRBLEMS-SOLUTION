class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column = len(matrix[0])
        left = 0
        right = len(matrix) * len(matrix[0]) -1
        while left <= right:
            mid = (left + right) // 2
            curr_row = mid // column
            curr_column = mid % column
            if matrix[curr_row][curr_column] < target:
                left  = mid + 1
            elif matrix[curr_row][curr_column] > target:
                right = mid - 1
            else:
                return True
        return False

