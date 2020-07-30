from collections import deque


def horizontal_orientation(left, right):
    return left[0] == right[0]


def visited(left, right, visited):
    lx, ly = left
    rx, ry = right
    if not (visited[lx][ly] and visited[rx][ry]):
        visited[lx][ly] = True
        visited[rx][ry] = True
        return False
    return True


def in_boundary(left, right, board):
    N = len(board)
    lx, ly = left
    rx, ry = right
    return 0 <= lx < N and 0 <= ly < N and 0 <= rx < N and 0 <= ry < N


def blocked(board, left, right, other=None):
    lx, ly = left
    rx, ry = right
    if other:
        ox, oy = other
        return board[lx][ly] == 1 or board[rx][ry] == 1 or board[ox][oy] == 1
    else:
        return board[lx][ly] == 1 or board[rx][ry]


def shift_move(left, right, board):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves = list()
    for ld, rd in zip(delta, delta):
        sh_left = (left[0] + ld[0], left[1] + ld[1])
        sh_right = (right[0] + rd[0], right[1] + rd[1])

        if not in_boundary(sh_left, sh_right, board):
            continue

        if blocked(board, sh_left, sh_right):
            continue

        moves.append((sh_left, sh_right))

    return moves


def rotate_move(left, right, board):
    moves = list()
    if horizontal_orientation(left, right):
        l_delta = [(0, 0), (0, 0), (1, 1), (-1, 1)]
        r_delta = [(1, -1), (-1, -1), (0, 0), (0, 0)]
        o_delta = [(1, 1), (-1, 1), (1, 0), (-1, 0)]
    else:
        l_delta = [(0, 0), (0, 0), (1, -1), (1, 1)]
        r_delta = [(-1, 1), (-1, -1), (0, 0), (0, 0)]
        o_delta = [(1, 1), (1, -1), (0, -1), (0, 1)]

    for ld, rd, od in zip(l_delta, r_delta, o_delta):
        rt_left = (left[0] + ld[0], left[1] + ld[1])
        rt_right = (right[0] + rd[0], right[1] + rd[1])
        other = (left[0] + od[0], left[1] + od[1])

        if not in_boundary(rt_left, rt_right, board):
            continue

        if blocked(board, rt_left, rt_right, other):
            continue

        rt_left, rt_right = min(rt_left, rt_right), max(rt_left, rt_right)
        moves.append((rt_left, rt_right))

    return moves


def solution(board):
    N = len(board)

    h_visited = [[False] * N for _ in range(N)]
    v_visited = [[False] * N for _ in range(N)]

    queue = deque([((0, 0), (0, 1))])
    counter = 0

    while queue:
        length = len(queue)
        for _ in range(length):
            left, right = queue.popleft()

            if left == (N-1, N-1) or right == (N-1, N-1):
                return counter

            for sh_left, sh_right in shift_move(left, right, board):
                if horizontal_orientation(sh_left, sh_right):
                    if not visited(sh_left, sh_right, h_visited):
                        queue.append((sh_left, sh_right))
                else:
                    if not visited(sh_left, sh_right, v_visited):
                        queue.append((sh_left, sh_right))
            for rt_left, rt_right in rotate_move(left, right, board):
                if horizontal_orientation(rt_left, rt_right):
                    if not visited(rt_left, rt_right, h_visited):
                        queue.append((rt_left, rt_right))
                else:
                    if not visited(rt_left, rt_right, v_visited):
                        queue.append((rt_left, rt_right))

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
