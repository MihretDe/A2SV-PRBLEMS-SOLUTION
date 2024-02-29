# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def preorder(root):
            if not root:
                return 
            answer.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        count = Counter(answer)
        mode = max(count.values())
        highest = []
        for key , value in count.items():
            if value == mode:
                highest.append(key)
        return highest
