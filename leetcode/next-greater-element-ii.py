class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = [-1] * (len(nums) * 2)
        nums2 = nums + nums
        for i in range(len(nums2)):
                while stack and stack[-1][0] < nums2[i]:
                    a = stack.pop()
                    next_greater[a[1]] = nums2[i]
                stack.append([nums2[i], i])
        return next_greater[:len(nums)]