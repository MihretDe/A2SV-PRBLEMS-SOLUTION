class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        l=0
        while l < len(nums):
            curr=nums[l]
            left = l+1
            right=len(nums)-1
            while left < right:
                if nums[left] + nums[right] < curr*-1:
                    left +=1
                elif nums[left] + nums[right] > curr*-1:
                    right-=1
                else:
                    ans=(curr,nums[left],nums[right])
                    res.append(ans)
                    left +=1
                    right-=1
            l+=1
        

            
        return set(res)



        
            

