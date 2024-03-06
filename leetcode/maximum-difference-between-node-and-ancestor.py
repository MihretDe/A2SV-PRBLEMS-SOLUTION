# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
       
        def find(root , min_root ,max_root ):
            if not root:
                return max_root -  min_root 
            min_root = min(min_root , root.val)
            max_root = max(max_root , root.val)
            left  = find(root.left , min_root ,max_root )
            right = find(root.right , min_root ,max_root)
            return max(left , right)
        return find(root , root.val , root.val)
            