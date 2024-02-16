class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len(set(nums))
        n = len(nums)
        complete = 0
        for i in range (n):
            set_nums = set()
            for j in range(i , n):
                set_nums.add(nums[j])
                if len(set_nums) == m:
                    complete +=1
        return complete

                