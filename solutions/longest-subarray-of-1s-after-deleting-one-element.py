class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        countd = 0
        left = 0
        right = 0
        length = 0
        while right < len(nums):
            if nums[right] != 1:
                countd += 1
            if countd > 1:
                while countd > 1 and left < len(nums):
                    if nums[left]!= 1:
                        countd -= 1
                    left+=1
            length = max(length, right - left)
            right += 1
        return length