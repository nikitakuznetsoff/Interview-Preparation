# Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_cube_id(x: int, y: int):
            return 3 * (x // 3) + (y // 3)

        vertical = {}
        horizontal = {}
        cubes = {}

        for i in range(len(board)):
            for j in range(len(board)):
                value = board[i][j]
                cube_id = get_cube_id(i, j)

                if value == ".":
                    continue

                if value in horizontal.get(i, []) \
                    or value in vertical.get(j, []) \
                    or value in cubes.get(cube_id, []):
                    return False

                horizontal[i] = horizontal.get(i, []) + [value]
                vertical[j] = vertical.get(j, []) + [value]
                cubes[cube_id] = cubes.get(cube_id, []) + [value]

        return True
