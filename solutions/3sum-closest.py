class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        closest_sum = float('inf')

        while l < len(nums) - 2:
            curr = nums[l]
            left = l + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[l] + nums[left] + nums[right]
                dist = abs(target - current_sum)

                if dist < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

            l += 1

        return closest_sum