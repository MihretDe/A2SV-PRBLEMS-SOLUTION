class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
    #    ''' 
    #     n=len(nums) // 3
    #     nums.sort()
    #     count=1
    #     if n == 0:
    #         return nums
    #     for i in range(len(nums)-1):
    #         if nums[i] == nums[i+1]:
    #             count += 1
    #         elif count > n :
    #             result.append(nums[i])
    #             count=0
    #         if count > n and i == len(nums)-2:
    #             result.append(nums[i])

    #     return result'''
        result=[]
        count = Counter(nums)
        for key,item in count.items():
            if item > len(nums) // 3:
                result.append(key)
        return result
