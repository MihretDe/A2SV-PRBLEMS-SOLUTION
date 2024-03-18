class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        min_length = len(nums)
        n = len(nums)
        prefix = 0
        dict_length = defaultdict()
        for i in range(n):
            prefix = (prefix + nums[i]) % p
            if prefix == target :
                min_length = min( min_length , i+1)
            
            if (prefix - target) % p in dict_length :
                min_length = min(min_length , i - dict_length[(prefix - target) % p])
            dict_length[prefix] = i
        if (min_length < n):
            return min_length 
        else:
            return  -1