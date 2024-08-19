from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            nonlocal kthNode, k

            if not node or k < 0:
                return

            helper(node.left)

            k -= 1

            if k == 0:
                kthNode = node.val
                return

            helper(node.right)

        kthNode = 0
        helper(root)
        return kthNode
