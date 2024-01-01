class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_nums = list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if string_nums[j] + string_nums[i] > string_nums[i] + string_nums[j] :
                    string_nums[j],string_nums[i]=string_nums[i],string_nums[j]
        val=int(''.join(string_nums))
        return str(val)

        
        



