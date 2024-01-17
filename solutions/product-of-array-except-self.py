class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1]
        pre = 1
        for i in range(len(nums)):
            pre*=nums[i]
            prefix.append(pre)
        suffix = []
        suff =1
        ans =[]
        for i in range(len(nums)-1 , -1 ,-1):
            suff*=nums[i]
            suffix.append(suff)
        suffix.reverse()
        suffix.append(1)
        left = 0
        right = 1
        while right < len(suffix):
            ans.append(suffix[right]* prefix[left])
            left += 1
            right +=1

            
        # print(prefix)
        # suffix.reverse()
        # suffix.append(1)

        # print(suffix)
        return ans
            
        
        