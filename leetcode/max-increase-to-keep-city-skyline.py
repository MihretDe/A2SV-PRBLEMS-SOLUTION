class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid1 = [[0] * len(grid) for n in range(len(grid))]
        row =[]
        for i in range(len(grid)):
            row.append(max(grid[i]))
        column = []
        for i in range(len(grid)):
            curr_max = 0
            for j in range(len(grid)):
                curr_max = max(curr_max , grid[j][i])
            column.append(curr_max)
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                grid1[i][j] = min(row[i] , column[j])
                total += grid1[i][j] - grid[i][j]
        
        return total
