class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        next_smaller = [-1] * (len(arr))
        for i in range(len(arr)):
                while stack and stack[-1][0] >= arr[i]:
                    a = stack.pop()
                    next_smaller[a[1]] = i
                stack.append([arr[i], i])
        print(next_smaller)
        stack =[]
        prev_smaller=[-1] * (len(arr))
        for i in range(0 , len(arr)):
            while stack and stack[-1][0] >= arr[i]:
                a = stack.pop()
            if stack :
                prev_smaller[i] = stack[-1][1]
            stack.append([arr[i] , i])
        print(prev_smaller)
        total = 0
        for i in range(len(prev_smaller)):
            if prev_smaller[i] == -1 and next_smaller[i] == -1:
                k = (i +1) * (len(arr) - i)
            elif next_smaller[i] == -1:
                k = (i - prev_smaller[i]) * (len(arr) - i)
            elif prev_smaller[i] == -1:
                k = (i+1) * (next_smaller[i] - i)
            else:
                k = (i - prev_smaller[i]) * (next_smaller[i] - i)
            total += (abs(k) * arr[i]) % (10**9 + 7)
            total %=(10**9 + 7)
            print(total)
        return total
        