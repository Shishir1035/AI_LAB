import random

def calculate_attacks(board):
    n = len(board)
    attacks = 0
    for row in range(n):
        for col in range(n):
            if row != col:
                if board[row] == board[col] or abs(board[row] - board[col]) == abs(row - col):
                    attacks += 1 

    return attacks

def generate_random_board(n):
    board = []
    for _ in range(n):
        board.append(random.randint(0, n - 1))
    return board

def hill_climbing(n, max_attempts=100):
    for _ in range(max_attempts):
        current_board = generate_random_board(n)
        print(current_board)
        current_attacks = calculate_attacks(current_board)

        while current_attacks > 0:
            neighbors = []
            for col in range(n):
                for row in range(n):
                    if current_board[col] != row:
                        neighbor = list(current_board)
                        neighbor[col] = row
                        neighbors.append(neighbor)

            best_neighbor = min(neighbors, key=calculate_attacks)
            best_attacks = calculate_attacks(best_neighbor)

            if best_attacks >= current_attacks:
                break

            current_board = best_neighbor
            current_attacks = best_attacks

        if current_attacks == 0:
            return current_board

    return None  


def print_solution(board):
    n = len(board)
    for row in range(n):
        line = []
        for col in range(n):
            if col == board[row]:
                line.append("Q")
            else:
                line.append(".")
        print(" ".join(line))

n = 8
solution = hill_climbing(n)

if solution is not None:
    print_solution(solution)
else:
    print("No solution found after multiple attempts.")
