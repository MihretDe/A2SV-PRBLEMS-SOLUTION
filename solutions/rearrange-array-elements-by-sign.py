class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive_num =[]
        negative_num = []
        result = []
        for num in nums:
            if num < 0:
                negative_num.append(num)
            else:
                postive_num.append(num)
        for i in range(len(nums)//2):
            result.append(postive_num[i])
            result.append(negative_num[i])
        return result



                
        