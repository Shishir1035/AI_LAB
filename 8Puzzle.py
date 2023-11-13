import heapq

def get_possible_moves(blank_position):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    poss_move = []
    for move in moves:
        if 0<=blank_position[0]+move[0]<3 and 0<=blank_position[1]+move[1]<3:
            poss_move.append((blank_position[0]+move[0], blank_position[1]+move[1]))

    return poss_move

def get_blank_position(puzzle):
    # print(puzzle)
    for i, row in enumerate(puzzle):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)

def get_neighbors(state):
    blank_position = get_blank_position(state)
    neighbors = []

    for move in get_possible_moves(blank_position):
        new_puzzle = [row[:] for row in state]
        new_puzzle[blank_position[0]][blank_position[1]], new_puzzle[move[0]][move[1]] = \
            new_puzzle[move[0]][move[1]], new_puzzle[blank_position[0]][blank_position[1]]
        
        neighbors.append(new_puzzle)
    return neighbors

def is_goal(state):
    # Check if the current state is the goal state
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal

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

def best_first_search(initial_state):
    heap = [(heuristic(initial_state), initial_state, [])]
    visited = set()

    while heap:
        cost, current_state, path = heapq.heappop(heap)

        if is_goal(current_state):
            print("Solution found in", len(path), "moves.")
            print_solution(path)
            return

        visited.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(heap, (heuristic(neighbor), neighbor, path + [neighbor]))

    print("No solution found.")

initial_puzzle = [[7, 2, 4],[5, 0, 6], [8, 3, 1]]
best_first_search(initial_puzzle)
