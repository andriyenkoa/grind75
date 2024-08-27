from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_res = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                cur_res = 1
                while num + 1 in set_nums:
                    num += 1
                    cur_res += 1
                max_res = max(max_res, cur_res)
        return max_res
