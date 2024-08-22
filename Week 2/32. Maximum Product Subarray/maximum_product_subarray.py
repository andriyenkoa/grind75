from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = global_product = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            global_product = max(max_product, global_product)

        return global_product
