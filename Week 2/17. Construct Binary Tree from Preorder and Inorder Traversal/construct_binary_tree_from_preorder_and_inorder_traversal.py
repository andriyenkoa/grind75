# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_idx_inorder = {val: idx for idx, val in enumerate(inorder)}

        self.preorder_idx = 0

        def helper(left, right):
            if left > right:
                return None

            inorder_idx = val_to_idx_inorder[preorder[self.preorder_idx]]
            self.preorder_idx += 1

            node = TreeNode(val=inorder[inorder_idx])

            node.left = helper(left, inorder_idx - 1)
            node.right = helper(inorder_idx + 1, right)
            return node

        root = helper(0, len(inorder) - 1)
        return root
