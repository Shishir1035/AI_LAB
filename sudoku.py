def is_valid(board, row, col, num):
    # Check if the number can be placed in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number can be placed in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find an empty location (0) in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location
    empty_loc = find_empty_location(board)
    
    # If there is no empty location, the Sudoku is solved
    if not empty_loc:
        return True
    
    row, col = empty_loc

    # Try placing numbers from 1 to 9 in the empty location
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number and recursively try to solve the rest
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If placing the number didn't lead to a solution, backtrack
            board[row][col] = 0

    # If no number can be placed, backtrack to the previous state
    return False

# Example Sudoku board (0 represents an empty cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku
if solve_sudoku(sudoku_board):
    # Print the solved Sudoku
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
