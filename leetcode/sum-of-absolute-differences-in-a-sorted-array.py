class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        prefix_sum = [0] * n
        postfix_sum = [0] * n
        prefix_sum[0] = nums[0]
        postfix_sum[-1] = nums[-1]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            postfix_sum[n - i - 1] = postfix_sum[n-i] + nums[n -i -1]
        
        for i in range(n):
            result.append(((nums[i] * i) - prefix_sum[i]) + (postfix_sum[i] - (nums[i] * (n - i -1))))
        return result 
