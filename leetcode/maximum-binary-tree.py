# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def max_ran(x , y):
            max_n = float('-inf')
            max_idx = -1
            for i in range(x , y+1):
                if nums[i] > max_n:
                    max_n = nums[i]
                    max_idx = i
            return max_idx
        def construct(x ,y):
            if x > y:
                return None
            z = max_ran(x , y)
            root = TreeNode(nums[z])
            root.left = construct(x , z-1)
            root.right = construct(z+1 , y)
            return root
        return construct(0 , len(nums) - 1)


