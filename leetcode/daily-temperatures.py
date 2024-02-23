class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        next_greater = [0] * len(temperatures)
        for i in range(len(temperatures)):
                while stack and stack[-1][0] < temperatures[i]:
                    a = stack.pop()
                    next_greater[a[1]] = i - a[1]
                stack.append([temperatures[i], i])
        return next_greater 
                

