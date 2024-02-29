# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1 , root2):
            if not root1 and  not root2:
                return None
            
            if not root1:
                return root2
            
            if not root2:
                return root1
            
            left = merge(root1.left ,root2.left )
            right = merge(root1.right , root2.right)
            # curr = TreeNode(root1.val + root2.val , left , right)
            root1.val += root2.val
            root1.left = left
            root1.right = right
            return root1
        return merge(root1 , root2)

