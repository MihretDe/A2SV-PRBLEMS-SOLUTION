from bisect import bisect_right
n = int(input())
nums = list(map(int , input().split()))
q = int(input())
nums.sort()
for i in range(q):
    m = int(input())
    ans = bisect_right(nums , m)
    print(ans)