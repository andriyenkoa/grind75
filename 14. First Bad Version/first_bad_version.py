# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    # Just for example
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return left
