class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = 0
                if i > 0:
                    curr+=self.prefix[i-1][j]
                if j > 0:
                    curr+=self.prefix[i][j-1]
                if i > 0 and j> 0:
                    curr-= self.prefix[i-1][j-1]
                curr+= matrix[i][j]
                self.prefix[i][j] = curr
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans =0
        ans +=self. prefix[row2][col2]
        if col1 > 0:
            print(1)
            ans-=self.prefix[row2][col1-1]
        if row1 > 0:
            ans -= self.prefix[row1-1][col2]
        if row1 > 0 and col1> 0:
            ans +=self.prefix[row1-1][col1-1]
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)