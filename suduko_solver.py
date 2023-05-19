import math
from grid import grid
def is_valid_move(grid, row, col, num):
    # Check row and column
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check the 3x3 grid
    x = int(math.sqrt(len(grid)))
    small_grid_row = (row // x) * x
    small_grid_col = (col // x) * x
    for i in range(x):
        for j in range(x):
            if grid[small_grid_row + i][small_grid_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 0:
                for num in range(1, len(grid) + 1):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        else:
                            grid[row][col] = 0
                return False
    return True

grid = [    [5, 3, 4, 0, 7, 8, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


if solve_sudoku(grid):
    for row in grid:
        print(row)
else:
    print("Cannot be solved")
