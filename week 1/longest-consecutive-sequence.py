class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count_num = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in count_num:
                current_num = num
                count = 0
                while current_num in count_num:
                    count += 1
                    current_num += 1
                longest = max(longest, count)
        return longest