# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        listp = []
        listq = []

        def search(root , p , listp):
            if root.val < p.val:
                listp . append(root)
                search(root.right , p , listp)
            elif root.val > p.val:
                listp . append(root)
                search(root.left , p , listp)
            else:
                listp .append(root)
                return listp

        search(root , p , listp)
        search(root , q , listq)
        
        set_q = set(listq)
        ans = []
        for i in range(len(listp)):
            if listp[i] in set_q:
                ans.append(listp[i])

        return ans[-1]
        




                