class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dict_num = Counter(nums)
        count0 = 0
        count1=dict_num[1]
        dict_freq = {}
        max_value = 0
        for i in range(len(nums) + 1):
            if i> 0 and nums[i-1]== 0:
                count0 += 1
            if i> 0 and nums[i-1] == 1:
                count1 -= 1
            dict_freq[i] = count0 + count1
            if count0 + count1 > max_value:
                max_value = count0 + count1
        max_keys = [k for k, v in dict_freq.items() if v == max_value]
        return(max_keys)
            

            
            
            





        