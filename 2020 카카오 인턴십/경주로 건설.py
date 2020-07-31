from collections import deque


def in_boundary(x, y, board):
    N = len(board)
    return 0 <= x < N and 0 <= y < N


def blocked(x, y, board):
    return board[x][y]


def calculate_cost(cost, orient, next_orient):
    if orient in ['L', 'R'] and next_orient in ['L', 'R']:
        return cost + 100
    elif orient in ['L', 'R'] and next_orient in ['U', 'D']:
        return cost + 600
    elif orient in ['U', 'D'] and next_orient in ['U', 'D']:
        return cost + 100
    elif orient in ['U', 'D'] and next_orient in ['L', 'R']:
        return cost + 600


def bfs(x, y, orient, cost, board):
    N = len(board)
    queue = deque([(x, y, orient, cost)])
    candidates = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
    cost_matrix = [[0] * N for _ in range(N)]

    while queue:
        x, y, orient, cost = queue.popleft()

        for dx, dy, o in candidates:
            if not in_boundary(x+dx, y+dy, board):
                continue
            if blocked(x+dx, y+dy, board):
                continue

            next_x = x + dx
            next_y = y + dy
            next_orient = o
            next_cost = calculate_cost(cost, orient, next_orient)

            if (not cost_matrix[next_x][next_y]) or\
                    (cost_matrix[next_x][next_y] > next_cost):
                cost_matrix[next_x][next_y] = next_cost
                queue.append([next_x, next_y, next_orient, next_cost])

    return cost_matrix[N-1][N-1]


def solution(board):
    cost_right = bfs(0, 0, 'R', 0, board)
    cost_down = bfs(0, 0, 'D', 0, board)

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
