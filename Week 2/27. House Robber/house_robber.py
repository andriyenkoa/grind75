from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums:
            return 0

        temp = [0] * (n + 1)
        temp[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            temp[i] = max(temp[i + 1], nums[i] + temp[i + 2])

        return temp[0]
