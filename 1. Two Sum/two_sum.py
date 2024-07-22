from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for idx in range(len(nums)):
            if nums[idx] in checked.keys():
                return [checked[nums[idx]], idx]
            else:
                checked[target - nums[idx]] = idx


if __name__ == "__main__":
    solution = Solution()
    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
