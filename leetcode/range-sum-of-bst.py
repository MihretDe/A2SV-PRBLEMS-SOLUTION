# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = []
        def call(root):
            if not root:
                return []
            call(root.left)
            answer.append(root.val)
            call(root.right)
        call(root)
        i = answer.index(low)
        j = answer.index(high) + 1
        return sum(answer[i:j])
