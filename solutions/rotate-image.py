class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_dict = {}
        for i in range(len(matrix)):
            row_dict[i] = matrix[i].copy() 
        
        l = len(matrix) - 1
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrix[j][i] = row_dict[l][j]
            l -= 1