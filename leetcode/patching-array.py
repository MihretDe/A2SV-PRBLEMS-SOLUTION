class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target =1
        r = 0
        ans= 0
        while target <=n :
            if r < len(nums) and nums[r] <= target:
                target+=nums[r]
                r+=1
            else:
                    target *=2
                    ans +=1
                    
        return ans 

            
            
        #     if nums[r] !=target:
        #         while r < len(nums) and target < nums[r]:
        #             target *=2
        #             if target < nums[r]:
        #                 ans +=1
        #         target +=nums[r]
        #     r+=1
        # if target < n:
        #     ans+=1
        # return ans

            
