from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [[intervals[0][0], intervals[0][1]]]

        for low, high in intervals:
            cur_high = result[-1][1]
            if low <= cur_high:
                result[-1][1] = max(cur_high, high)
            else:
                result.append([low, high])

        return result
