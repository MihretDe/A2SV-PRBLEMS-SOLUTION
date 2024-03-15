class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        nums.sort()
        count = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -=1
            else:
                count += pow(2 , (right - left) , (10**9 + 7))
                count = count % (10**9 + 7)
                left +=1
        return count % (10**9 + 7)
            