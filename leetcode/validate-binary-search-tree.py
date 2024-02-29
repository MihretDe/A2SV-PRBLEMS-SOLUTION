# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            array.append(root.val)
            inorder(root.right)
        inorder(root)
        sorted_array = sorted(array)
        return sorted_array == array and len(array) == len(set(array))