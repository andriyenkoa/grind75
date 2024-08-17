from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def helper(r, c, letter_idx):
            if letter_idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[letter_idx]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            for r_s, c_s in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if helper(r + r_s, c + c_s, letter_idx + 1):
                    return True

            board[r][c] = temp

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if helper(i, j, 0):
                        return True

        return False
