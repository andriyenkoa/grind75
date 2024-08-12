# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.depth = []
        self.traverse(root, 0)
        return self.depth

    def traverse(self, node: Optional[TreeNode], cur_depth) -> int:
        if not node:
            return
        if node:
            if cur_depth < len(self.depth):
                self.depth[cur_depth].append(node.val)
            else:
                self.depth.append([node.val])

        self.traverse(node.left, cur_depth + 1)
        self.traverse(node.right, cur_depth + 1)

