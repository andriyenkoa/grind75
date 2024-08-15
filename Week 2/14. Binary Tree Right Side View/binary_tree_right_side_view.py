from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.max_depth = 0
        self.res = []

        def dfs(node, cur_depth):
            if not node:
                return
            if cur_depth > self.max_depth:
                self.max_depth = max(cur_depth, self.max_depth)
                self.res.append(node.val)
            dfs(node.right, cur_depth + 1)
            dfs(node.left, cur_depth + 1)

        dfs(root, 1)
        return self.res
