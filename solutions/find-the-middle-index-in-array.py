class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix =[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        suffix =[]
        for i in range(len(nums)):
            suffix.append(prefix[-1] - prefix[i])
        for i in range(len(nums)):
            if prefix[i] - nums[i] == suffix[i]:
                return i
        return -1