class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
                continue
            if nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i] > stack[-1]:
                    p=stack.pop()
                    ans[nums2.index(p)] = nums2[i]
                stack.append(nums2[i])
        print(ans)
        result = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            result.append(ans[j])
        return result





        # ans  =[]
        # for i in range(len(nums1)):
        #     j = nums2.index(nums1[i])
        #     if j < len(nums2)-1 and nums1[i] < nums2[j+1]:
        #         ans .append(nums2[j+1])
        #     else:
        #         ans.append(-1)
        # return ans 