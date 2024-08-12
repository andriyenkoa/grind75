from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.to_check = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.traverse(grid, r, c)
                    result += 1

        return result

    def traverse(self, grid, r, c):
        if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1:
            return

        if grid[r][c] != "1":
            return

        grid[r][c] = "2"
        for one_check in self.to_check:
            self.traverse(grid, r + one_check[0], c + one_check[1])
