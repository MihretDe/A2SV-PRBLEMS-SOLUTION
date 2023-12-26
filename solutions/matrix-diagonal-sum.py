class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i -j==0:
                    sum1 += mat[i][j]
                elif i+j == len(mat) -1:
                    sum1 += mat[i][j]
        return sum1
        # i=0
        # j=0
        # while i<len(mat) and j<len(mat):
        #     sum1 += mat[i][j]
        #     i+=1
        #     j+=1

        # i=0
        # j=len(mat)-1
        # while i<len(mat) and j>-1:
        #     if i==j:
        #         i+=1
        #         j-=1
        #         continue
        #     sum1 += mat[i][j]
        #     i+=1
        #     j-=1
        # return sum1

