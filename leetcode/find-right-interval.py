class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        for i in range(len(intervals)):
            start.append((intervals[i][0] , i))
        answer = [-1] * len(intervals)
        start.sort()
        for i in range(len(intervals)):
            left = 0 
            right = len(intervals) - 1
            target  = intervals[i][1]
            ans = float(inf)
            while left <= right:
                mid = (left + right) // 2
                if start[mid][0] >= target:
                    ans = start[mid][1]
                    right = mid -1
                else:
                    left = mid + 1
            if ans!=float(inf):
                answer[i] = ans
        return answer
            
                