class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
        
            if i == nums[i] :
                i += 1
            else:
                p = nums[i] 
                if p == len(nums):
                    i +=1
                else:
                    nums[i] , nums[p] = nums[p] ,  nums[i]
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
        
        