# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.counter(root)
        return self.max

    def counter(self, node: Optional[TreeNode]) -> int:
        left = self.counter(node.left) if node.left else 0
        right = self.counter(node.right) if node.right else 0
        self.max = max(self.max, left + right)
        return 1 + max(left, right)
