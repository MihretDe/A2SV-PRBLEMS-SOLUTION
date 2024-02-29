# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # def sum1(root):
        #     if not root.left:
        #         return root.val
        #     left = str(root.val) + str(sum1(root.left))
        #     right = str(root.val) + str(sum1(root.right))
        #     return [left , right]
        # if not root.left:
        #     return root.right
        # if not root.right:
        #     return root.left
        # ans= sum1(root)
        # print(ans)
        # return 0
        # # return int(a) + int(b)
        def sum1(root , val):
            if not root:
                return 0
            if not root.left and not root.right :
                return val*10 + root.val
            val = val*10 + root.val
            return sum1(root.left , val) + sum1(root.right, val)
        return sum1(root , 0)

            