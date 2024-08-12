from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        minutes_passed = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                rotten_row, rotten_col = queue.popleft()
                for row_step, col_step in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row, new_col = rotten_row + row_step, rotten_col + col_step
                    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                        continue
                    if grid[new_row][new_col] == 2 or grid[new_row][new_col] == 0:
                        continue
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
                    fresh -= 1
        print(fresh)
        return minutes_passed if fresh == 0 else -1
