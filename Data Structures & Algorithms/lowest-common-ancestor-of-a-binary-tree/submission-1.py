# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs (emphasize recursion) [stack]
        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        # elif (root.left and root.right) and (root.left.val == p.val and root.right.val == q.val):
        #     return root
        # elif (root.left and root.right) and (root.right.val == p.val and root.left.val == q.val):
        #     return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l or r
        

        