# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count  = defaultdict(list)
        def level_traversal(root , level):
            if not root:
                return
            count[level] . append(root.val)

            level_traversal(root.left , level+1)
            level_traversal(root.right , level+1)
        level = 0
        level_traversal(root , level)
        answer = []
        for key , value in count.items():
            if key%2 ==1:
                value.reverse()
            answer.append(value)
        return answer 
            