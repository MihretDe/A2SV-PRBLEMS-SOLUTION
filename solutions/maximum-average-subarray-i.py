class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=sum(nums[:k])
        left = 0
        right = k
        max_avg = float(sum1) / k 
        while right < len(nums):
            sum1 += nums[right]
            sum1 -= nums[left]
            max_avg = max(max_avg , float(sum1) / k)
            left += 1
            right += 1
        return max_avg



        