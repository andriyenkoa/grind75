# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, cur_path, cur_sum):
            if not node:
                return
            cur_path.append(node.val)
            cur_sum += node.val
            if node.left:
                dfs(node.left, cur_path, cur_sum)
            if node.right:
                dfs(node.right, cur_path, cur_sum)
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    res.append(cur_path.copy())
            cur_path.pop()
            cur_sum -= node.val
        dfs(root, [], 0)
        return res
