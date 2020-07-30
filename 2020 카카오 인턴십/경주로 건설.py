from collections import deque


def in_boundary(x, y, board):
    N = len(board)
    return 0 <= x < N and 0 <= y < N


def blocked(x, y, board):
    return board[x][y]


def calculate_cost(base_cost, base_direction, direction):
    if base_direction in ['L', 'R'] and direction in ['L', 'R']:
        return base_cost + 100
    elif base_direction in ['U', 'D'] and direction in ['U', 'D']:
        return base_cost + 100
    elif base_direction in ['L', 'R'] and direction in ['U', 'D']:
        return base_cost + 600
    elif base_direction in ['U', 'D'] and direction in ['L', 'R']:
        return base_cost + 600


def bfs(x, y, direction, board):
    N = len(board)
    cost_matrix = [[0] * N for _ in range(N)]

    queue = deque([(x, y, 0, direction)])
    while queue:
        x, y, c, d = queue.popleft()
        for dx, dy, direction in\
                [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]:
            next_x = x + dx
            next_y = y + dy

            if not in_boundary(next_x, next_y, board):
                continue

            if blocked(next_x, next_y, board):
                continue

            next_c = calculate_cost(c, d, direction)
            if not cost_matrix[next_x][next_y] or\
                    cost_matrix[next_x][next_y] > next_c:
                cost_matrix[next_x][next_y] = next_c
                queue.append((next_x, next_y, next_c, direction))

    return cost_matrix[N-1][N-1] if cost_matrix[N-1][N-1] else -1


def solution(board):
    cost_right = bfs(0, 0, 'R', board)
    cost_down = bfs(0, 0, 'D', board)
    return min(max(0, cost_right), max(0, cost_down))


if __name__ == "__main__":
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert solution(board) == 900

    board = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 3800

    board = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 0]
    ]
    assert solution(board) == 2100

    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 3200
