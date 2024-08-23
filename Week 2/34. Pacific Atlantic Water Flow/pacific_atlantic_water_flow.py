from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        def dfs(row, col, touchesOcean, prevHeight):
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or (row, col) in touchesOcean:
                return

            if heights[row][col] >= prevHeight:
                touchesOcean.add((row, col))

                for row_step, col_step in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(row + row_step, col + col_step, touchesOcean, heights[row][col])

        for i in range(len(heights)):
            dfs(i, 0, pacific_set, 0)
            dfs(i, len(heights[0]) - 1, atlantic_set, 0)

        for i in range(len(heights[0])):
            dfs(0, i, pacific_set, 0)
            dfs(len(heights) - 1, i, atlantic_set, 0)

        return list(pacific_set & atlantic_set)
