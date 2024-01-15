class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count_odd = 0
        nice_sub = 0
        nice_prev = 0

        while right < len(nums):
            if nums[right] % 2 == 1:
                count_odd += 1
            while count_odd > k and left < right:
                if nums[left] % 2 == 1:
                    count_odd -= 1
                left += 1
            if count_odd <= k:
                nice_sub += right - left + 1
            
            right += 1

        left = 0
        right = 0
        count_odd = 0

        while right < len(nums):
            if nums[right] % 2 == 1:
                count_odd += 1
            while count_odd > k - 1 and left < right:
                if nums[left] % 2 == 1:
                    count_odd -= 1
                left += 1
            if count_odd <= k - 1:
                nice_prev += right - left +1
            
            right += 1

        return nice_sub - nice_prev