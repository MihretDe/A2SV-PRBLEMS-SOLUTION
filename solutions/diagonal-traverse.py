class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        count = 0
        res = []
        for i in range(len(mat[0])):
            curr  = []
            j = 0
            while j<len(mat) and i > -1:
                curr.append(mat[j][i])
                j += 1
                i -= 1
            if count % 2 == 0:
                res.extend(reversed(curr))
            else:
                res.extend(curr) 
            count += 1

        for j in range(1,len(mat)):
            curr = []
            i = len(mat[0] ) -1
            while j<len(mat) and i > -1:
                curr.append(mat[j][i])
                j += 1
                i -= 1
            if count % 2 == 0:
                res.extend(reversed(curr))
            else:
                res.extend(curr) 
            count += 1
        return res



        