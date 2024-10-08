from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1

#[ 0, 1, 2, 3, 4,  5]
#[-1, 0, 3, 5, 9, 12]