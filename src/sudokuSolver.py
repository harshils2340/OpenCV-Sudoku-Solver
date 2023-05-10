def solve_sudoku(grid):
    row, col = find_empty_cell(grid)
    
    if row == -1 and col == -1:
        return True
    
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0
            
    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return -1, -1

def is_valid_move(grid, row, col, num):
    # check row
    for j in range(9):
        if grid[row][j] == num:
            return False
    
    # check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # check sub-grid
    sub_grid_row = (row // 3) * 3
    sub_grid_col = (col // 3) * 3
    
    for i in range(sub_grid_row, sub_grid_row + 3):
        for j in range(sub_grid_col, sub_grid_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku_wrapper(grid):
    if solve_sudoku(grid):
        for row in grid:
            print(row)
    else:
        print("Not solvable")

