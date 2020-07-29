from collections import deque


def visited(left, right, visited):
    if visited[left[0]][left[1]] and visited[right[0]][right[1]]:
        return True
    else:
        visited[left[0]][left[1]] = True
        visited[right[0]][right[1]] = True
        return False


def is_horizontal(left, right):
    return left[0] == right[0]


def check_boundary_valid(left, right, N):
    return 0 <= left[0] < N and 0 <= left[1] < N and 0 <= right[0] < N and 0 <= right[1] < N


def check_blocked_valid(board, left, right, other=None):
    if other:
        return board[left[0]][left[1]] == 0 and board[right[0]][right[1]] == 0 and board[other[0]][other[1]] == 0
    else:
        return board[left[0]][left[1]] == 0 and board[right[0]][right[1]] == 0


def valid_move(left, right, board):
    N = len(board)

    if not check_boundary_valid(left, right, N):
        return False
    if not check_blocked_valid(left, right, board):
        return False

    return True


def shift(left, right, board):
    N = len(board)
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    locations = list()
    for dl, dr in zip(delta, delta):
        left_shifted = (left[0] + dl[0], left[1] + dl[1])
        right_shifted = (right[0] + dr[0], right[1] + dr[1])

        if not check_boundary_valid(left_shifted, right_shifted, N):
            continue

        if not check_blocked_valid(board, left_shifted, right_shifted):
            continue

        locations.append((left_shifted, right_shifted))

    return locations


def rotate(left, right, board):
    locations = list()
    N = len(board)

    if is_horizontal(left, right):
        delta_left = [(0, 0), (0, 0), (-1, 1), (1, 1)]
        delta_right = [(-1, -1), (1, -1), (0, 0), (0, 0)]
        delta_other = [(-1, 1), (1, 1), (-1, 0), (1, 0)]
    else:
        delta_left = [(0, 0), (0, 0), (1, 1), (1, -1)]
        delta_right = [(-1, 1), (-1, -1), (0, 0), (0, 0)]
        delta_other = [(1, 1), (1, -1), (0, 1), (0, -1)]

    for dl, dr, do in zip(delta_left, delta_right, delta_other):
        left_rotated = (left[0] + dl[0], left[1] + dl[1])
        right_rotated = (right[0] + dr[0], right[1] + dr[1])
        left_rotated, right_rotated = min(left_rotated, right_rotated), max(left_rotated, right_rotated)
        other = (left[0] + do[0], left[1] + do[1])

        if not check_boundary_valid(left_rotated, right_rotated, N):
            continue

        if not check_blocked_valid(board, left_rotated, right_rotated, other):
            continue

        locations.append((left_rotated, right_rotated))

    return locations


def solution(board):
    N = len(board)
    left = (0, 0)
    right = (0, 1)

    location = (left, right)

    counter = 0

    queue = deque([location])

    visited_horizontal = [[False] * (N) for _ in range(N)]
    visited_vertical = [[False] * (N) for _ in range(N)]

    visited_horizontal[0][0] = True
    visited_horizontal[0][1] = True

    while queue:
        length = len(queue)

        for _ in range(length):
            left, right = queue.popleft()
            if left == (N-1, N-1) or right == (N-1, N-1):
                return counter

            for left_shifted, right_shifted in shift(left, right, board):
                if is_horizontal(left_shifted, right_shifted):
                    if not visited(left_shifted, right_shifted, visited_horizontal):
                        queue.append((left_shifted, right_shifted))
                else:
                    if not visited(left_shifted, right_shifted, visited_vertical):
                        queue.append((left_shifted, right_shifted))

            for left_rotated, right_rotated in rotate(left, right, board):
                if is_horizontal(left_rotated, right_rotated):
                    if not visited(left_rotated, right_rotated, visited_horizontal):
                        queue.append((left_rotated, right_rotated))
                else:
                    if not visited(left_rotated, right_rotated, visited_vertical):
                        queue.append((left_rotated, right_rotated))

        counter += 1

    return -1


if __name__ == "__main__":
    board = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    assert solution(board) == 7
