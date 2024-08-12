from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()

        for num in nums:
            if num in checked:
                return True
            checked.add(num)

        return False
