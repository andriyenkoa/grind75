from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]

        multiply = 1
        for i in range(len(nums)):
            result[i] *= multiply
            multiply *= nums[i]

        multiply = 1
        for i in reversed(range(len(nums))):
            result[i] *= multiply
            multiply *= nums[i]

        return result
