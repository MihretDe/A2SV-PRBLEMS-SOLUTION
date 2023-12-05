class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points)-1):
            x_time = abs(points[i][0]-points[i+1][0])
            y_time = abs(points[i][1]-points[i+1][1])
            total_time += max( x_time, y_time )
        return total_time


        