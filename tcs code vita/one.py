from collections import deque

def min_moves_to_reach_destination(grid, M, N, source, destination, move_rule):
    directions = [
        move_rule,                
        (move_rule[1], -move_rule[0]),   
        (-move_rule[1], move_rule[0]),   
        (-move_rule[0], -move_rule[1])   
    ]

    queue = deque([(source[0], source[1], 0)])  # (row, col, moves)
    visited = set()
    visited.add((source[0], source[1]))

    while queue:
        row, col, moves = queue.popleft()
        
        if (row, col) == destination:
            return moves

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < M and 0 <= new_col < N and 
                grid[new_row][new_col] == 0 and (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, moves + 1))

    return -1

# Read input
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
source = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))
move_rule = tuple(map(int, input().split()))

# Print the result
print(min_moves_to_reach_destination(grid, M, N, source, destination, move_rule))
