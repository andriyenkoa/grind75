from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_res = 0

        while left < right:
            cur_res = min(height[left], height[right]) * (right - left)
            max_res = max(max_res, cur_res)
            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
                right -= 1

        return max_res