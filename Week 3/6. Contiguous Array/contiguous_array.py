from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        max_len = 0
        table = {0:0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                diff -= 1
            else:
                diff += 1
            if diff in table:
                max_len = max(max_len, index - table[diff])
            else:
                table[diff] = index
        return max_len
