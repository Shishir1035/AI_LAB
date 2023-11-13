
num_step = 0

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)

    #print(start_row, start_col)

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: 
                for num in range(1, 10): 
                    global num_step
                    num_step += 1
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            
                            return True
                        board[row][col] = 0 
                return False
    return True


initial_state = [
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

empty_cell = 0

for i in range(9):
    for j in range(9):
        if initial_state[i][j] == 0:
            empty_cell += 1

if solve_sudoku(initial_state):
    print("Sudoku Solution:")
    print('Empty cell ', empty_cell)
    print('Number of step ', num_step)
    print_sudoku(initial_state)
else:
    print("No solution exists for the given Sudoku puzzle.")
