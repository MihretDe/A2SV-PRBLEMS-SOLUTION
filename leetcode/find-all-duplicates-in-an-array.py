class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
        
            if i == nums[i] - 1:
                i += 1
            else:
                p = nums[i] - 1
                if p == nums[p] - 1:
                    if nums[i] not in ans:
                        ans.append(nums[i])
                    i += 1
                else:
                    nums[i] , nums[p] = nums[p] ,  nums[i]
        return ans
        