class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):
            curr = []
            for j in range(len(matrix)):
                curr.append(matrix[j][i])
            result.append(curr)
        return result

        