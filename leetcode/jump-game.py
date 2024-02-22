class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            step = max( step , i + nums[i])
            if step == i:
                return False
        if step < len(nums)-1:
            return False
        return True