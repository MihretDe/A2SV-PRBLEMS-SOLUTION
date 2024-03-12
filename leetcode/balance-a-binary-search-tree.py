# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def BST(l , r):
            if l > r:
                return None
            mid = (l+r) //2
            left = BST(l , mid -1)
            right = BST(mid +1 , r)
            return TreeNode(nums[mid] , left , right)
        
        nums = []
        def call(root):
            if not root:
                return []
            call(root.left)
            nums.append(root.val)
            call(root.right)
        call(root)

        return BST(0 , len(nums)-1)