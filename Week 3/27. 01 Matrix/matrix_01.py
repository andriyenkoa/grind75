from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        sum_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row_len = len(mat)
        col_len = len(mat[0])
        queue = deque()

        for r in range(row_len):
            for c in range(col_len):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1

        while queue:
            r, c = queue.popleft()

            for i in range(len(sum_list)):
                new_r = r + sum_list[i][0]
                new_c = c + sum_list[i][1]

                if new_r < 0 or new_r == row_len or new_c < 0 or new_c == col_len or mat[new_r][new_c] != -1:
                    continue
                mat[new_r][new_c] = mat[r][c] + 1
                queue.append((new_r, new_c))

        return mat
