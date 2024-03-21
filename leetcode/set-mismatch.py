class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
        
            if i == nums[i] - 1:
                i += 1
            else:
                p = nums[i] - 1
                if p == nums[p] - 1:
                    i += 1
                else:
                    nums[i] , nums[p] = nums[p] ,  nums[i]
        
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(nums[i])
                ans.append(i+1)
        return ans