# Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def change_coord(x, y, left_side, right_side):
            return y, right_side - x + left_side

        start_x, start_y = 0, 0
        x, y = 0, 0
        saved = matrix[0][0]

        for step in range(len(matrix) - 1, 0, -2):
            for i in range(step * 4):
                x, y = change_coord(x, y, start_x, start_x + step)
                matrix[x][y], saved = saved, matrix[x][y]
                if x == start_x and y == start_y:
                    y += 1
                    saved = matrix[x][y]
                    start_x, start_y = x, y
            x += 1
            y = x
            start_x, start_y = x, y
            saved = matrix[x][y]
