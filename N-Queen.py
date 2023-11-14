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

def hill_climbing(n, max_attempts=100):
    for _ in range(max_attempts):
        current_board = generate_random_board(n)
        # print(current_board)
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

n = 8
solution = hill_climbing(n)

if solution is not None:
    print_solution(solution)
else:
    print("No solution found after multiple attempts.")


# import random

# def initialize_board(size):
#     """Initialize a random placement of queens on the board."""
#     return [random.randint(0, size - 1) for _ in range(size)]

# def calculate_attacks(board):
#     """Calculate the total number of queen attacks on the board."""
#     size = len(board)
#     attacks = 0
#     for i in range(size):
#         for j in range(size):
#             if i != j and (board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j)):
#                 attacks += 1
#     return attacks

# def generate_neighbors(board):
#     """Generate neighboring states by moving one queen to a different row."""
#     neighbors = []
#     size = len(board)
#     for i in range(size):
#         for j in range(size):
#             if j != board[i]:
#                 neighbor = board.copy()
#                 neighbor[i] = j
#                 neighbors.append(neighbor)
#     return neighbors

# def beam_search(size, beam_width, max_iterations):
#     """Solve the N-Queens problem using beam search."""
#     current_board = initialize_board(size)
#     current_attacks = calculate_attacks(current_board)

#     for _ in range(max_iterations):
#         neighbors = generate_neighbors(current_board)
#         neighbors_with_attacks = [(neighbor, calculate_attacks(neighbor)) for neighbor in neighbors]
#         neighbors_with_attacks.sort(key=lambda x: x[1])
#         best_neighbors = neighbors_with_attacks[:beam_width]

#         if best_neighbors[0][1] == 0:
#             return best_neighbors[0][0]  # Solution found

#         next_board = random.choice(best_neighbors)[0]
#         next_attacks = calculate_attacks(next_board)

#         if next_attacks < current_attacks:
#             current_board = next_board
#             current_attacks = next_attacks

#     return None  # No solution found within the maximum iterations

# def print_solution(board):
#     """Print the N-Queens solution."""
#     size = len(board)
#     for i in range(size):
#         row = ['Q' if j == board[i] else '.' for j in range(size)]
#         print(" ".join(row))
#     print()

# # Example usage
# n_queens_size = 8
# beam_width = 2
# max_iterations = 1000
# solution = beam_search(n_queens_size, beam_width, max_iterations)

# if solution:
#     print("Solution found:")
#     print_solution(solution)
# else:
#     print("No solution found within the maximum iterations.")
