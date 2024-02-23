class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = []
        prefix.append(nums[0])
        for i in range(1,len(nums)):
            pre= prefix[i-1] + nums[i]
            prefix.append(pre)
        
        for i in range(len(nums)):
            prefix[i] = ceil(prefix[i] / (i+1))
        return max(prefix)