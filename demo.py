
import heapq

def get_possible_moves(blank_position):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    poss_move = []
    for move in moves:
        if 0 <= blank_position[0] + move[0] < 3 and 0 <= blank_position[1] + move[1] < 3:
            poss_move.append((blank_position[0] + move[0], blank_position[1] + move[1]))

    return poss_move

def get_blank_position(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return (i, j)

def is_goal(state):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal

def get_neighbors(state, cost_so_far):
    blank_position = get_blank_position(state)
    neighbors = []

    for move in get_possible_moves(blank_position):
        new_puzzle = [row[:] for row in state]
        new_puzzle[blank_position[0]][blank_position[1]], new_puzzle[move[0]][move[1]] = \
            new_puzzle[move[0]][move[1]], new_puzzle[blank_position[0]][blank_position[1]]

        # Calculate the cost to reach this neighbor
        new_cost = cost_so_far + 1  # Assuming each move has a cost of 1

        neighbors.append((new_cost + heuristic(new_puzzle), new_cost, new_puzzle))

    return neighbors

def print_solution(path):
    for step in path:
        print("\n".join(" ".join(map(str, row)) for row in step))
        print()

def heuristic(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                row, col = divmod(puzzle[i][j] - 1, 3)
                distance += abs(i - row) + abs(j - col)
    return distance

def astar_search(initial_state):
    heap = [(heuristic(initial_state), 0, initial_state, [])]
    visited = set()

    while heap:
        _, cost_so_far, current_state, path = heapq.heappop(heap)

        if is_goal(current_state):
            print("Solution found in", len(path), "moves.")
            print_solution(path)
            return

        visited.add(tuple(map(tuple, current_state)))

        for _, new_cost, neighbor in get_neighbors(current_state, cost_so_far):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(heap, (new_cost + heuristic(neighbor), new_cost, neighbor, path + [neighbor]))

    print("No solution found.")

initial_puzzle = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
astar_search(initial_puzzle)
