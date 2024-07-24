# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root

        while True:
            if temp.val == p.val or temp.val == q.val:
                return temp
            if p.val < temp.val and q.val < temp.val:
                temp = temp.left
            elif p.val > temp.val and q.val > temp.val:
                temp = temp.right
            else:
                return temp
