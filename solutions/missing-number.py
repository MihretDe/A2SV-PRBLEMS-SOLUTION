class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #for i in range(len(nums)+1):
          #  if i not in nums:
             #   return i
        nums_set = set(nums)
        for i in range(len(nums_set)+1):
          if i not in nums_set:
            return i

        