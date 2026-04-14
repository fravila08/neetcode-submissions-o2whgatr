# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def switch(curr):
            if not curr:
                return
            dummy = curr.left
            curr.left = curr.right
            curr.right = dummy
            switch(curr.left)
            switch(curr.right)
        switch(root)
        return root