class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        length = 0
        count0 =0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            if count0 > k:
                while count0 > k and left < len(nums):
                    if nums[left] == 0:
                        count0 -= 1
                    left += 1
            length = max(length , i - left+1)
            
        return length