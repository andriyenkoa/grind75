from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(cur, used):
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            for i, letter in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                cur.append(letter)
                dfs(cur,used)
                cur.pop()
                used[i] = False

        dfs([], [False] * len(nums))
        return result
