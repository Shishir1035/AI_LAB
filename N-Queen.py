import random

#returns a list which denotes the queen position in the ith row (0 base)
def initialize_board(size):
    board = []
    for _ in range(size):
        board.append(random.randint(0, size-1))
    print(board)
    return board

def calculate_attacks(board):
    size = len(board)
    attacks = 0
    for i in range(size):
        for j in range(i+1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def print_board(board):
    size = len(board)
    for row in range(size):
        line = []
        for col in range(size):
            if col == board[row]:
                line.append('Q')
            else:
                line.append('.')
        
        #concate list to a string
        print(" ".join(line))
    print()

def hill_climbing(size, max_iterations=800000):
    current_board = initialize_board(size)
    current_attacks = calculate_attacks(current_board)

    for _ in range(max_iterations):
        if current_attacks == 0:
            print("Solution found:")
            print_board(current_board)
            return current_board

        new_board = current_board.copy()
        random_row = random.randint(0, size-1)
        random_col = random.randint(0, size-1)
        new_board[random_row] = random_col

        # Calculate attacks in the neighboring state
        neighbor_attacks = calculate_attacks(new_board)

        # If the neighboring state has fewer attacks, move to that state
        if neighbor_attacks < current_attacks:
            current_board = new_board
            current_attacks = neighbor_attacks

    print("Solution not found.")
    return None

n_queens_size = 4
hill_climbing(n_queens_size)
