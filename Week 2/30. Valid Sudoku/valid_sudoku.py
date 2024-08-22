from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRows(board) and self.isValidCols(board) and self.isValidSquare(board)

    def isValidRows(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True

    def isValidCols(self, board: List[List[str]]) -> bool:
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        return True

    def isValidSquare(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValidUnit(square):
                    return False
        return True

    def isValidUnit(self, unit: List[str]) -> bool:
        clear_unit = [el for el in unit if el != "."]
        return len(set(clear_unit)) == len(clear_unit)
