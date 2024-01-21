class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*len(nums)
        for request in requests:
            prefix[request[0]]+=1
            if request[1] < len(nums) -1:
                prefix[request[1] + 1]-=1
        arr = [prefix[0]]
        for i in range(1,len(prefix)):
            arr.append(arr[i-1]+prefix[i])
        nums.sort()
        arr.sort()
        res =0
        for i in range(len(nums)):
            res += nums[i] * arr[i]

        return res % (10**9 + 7)
        

        
        
