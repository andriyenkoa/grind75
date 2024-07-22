from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        self.changeColor(image, sr, sc, color, image[sr][sc])
        return image

    def changeColor(self, image: List[List[int]], sr: int, sc: int, color: int, cur: int) -> None:
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return

        if image[sr][sc] != cur:
            return

        image[sr][sc] = color

        self.changeColor(image, sr - 1, sc, color, cur)
        self.changeColor(image, sr + 1, sc, color, cur)
        self.changeColor(image, sr, sc - 1, color, cur)
        self.changeColor(image, sr, sc + 1, color, cur)


if __name__ == "__main__":
    solution = Solution()
    assert solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2) == [[2, 2, 2], [2, 2, 0],
                                                                                                [2, 0, 1]]
    assert solution.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0) == [[0, 0, 0], [0, 0, 0]]
