class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        x = 0
        ans =1
        for i in range(len(points)):
            y = points[x][1]
            if points[i][0] > y:
                x=i
                ans +=1
            else:
                # y = min(y ,points[i][1] )
                if y > points[i][1]:
                    x =i
        return ans 
                


