class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(1,len( nums)):
        #     for j in range(i,0,-1):
        #         if nums[j] <  nums[j-1]:
        #             nums[j],nums[j-1]=nums[j-1],nums[j]
        left=0
        while left < len(nums):
            if nums[left] ==0:
                left+=1
                continue
            else:
                right=left+1
                while nums[left]!=[0] and right<len(nums):
                    if nums[right] < nums[left]:
                        nums[right],nums[left]=nums[left], nums[right]
                    right+=1
            left+=1
            