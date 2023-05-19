def is_valid_move(grid, row, col, num):
    # Check row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    # Check the 3x3 grid
    small_grid_row = (row // 3) * 3
    small_grid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[small_grid_row + i][small_grid_col + j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Undo the move
                return False
    return True

grid = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0]
]

solve_sudoku(grid)

for row in grid:
    print(row)
