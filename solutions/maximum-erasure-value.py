class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        unique_num = set()
        num_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in unique_num:
                unique_num.add(nums[i])
                num_sum += nums[i]
            else:
                while nums[i]  in unique_num:
                    unique_num.remove(nums[left])
                    num_sum -= nums[left]
                    left += 1
                unique_num.add(nums[i])
                num_sum += nums[i]
            ans = max(ans , num_sum)
        return ans