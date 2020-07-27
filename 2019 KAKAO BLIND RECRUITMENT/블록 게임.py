def fill_board(board, N):
    for cdx in range(N):
        for rdx in range(N):
            if board[rdx][cdx] <= 0:
                board[rdx][cdx] = -1
            else:
                break


def possible_to_delete(base_rdx, base_cdx, board, N, shape):
    if base_rdx + shape[0] > N or base_cdx + shape[1] > N:
        return False

    target = board[base_rdx][base_cdx]
    if target == -1:
        for rdx in range(base_rdx, base_rdx+shape[0]):
            for cdx in range(base_cdx, base_cdx+shape[1]):
                if board[rdx][cdx] > 0:
                    target = board[rdx][cdx]
                    break
    if target <= 0:
        return False

    n_target = 0

    for rdx in range(base_rdx, base_rdx+shape[0]):
        for cdx in range(base_cdx, base_cdx+shape[1]):
            if board[rdx][cdx] == 0:
                return False
            if board[rdx][cdx] > 0 and board[rdx][cdx] != target:
                return False

            if board[rdx][cdx] == target:
                n_target += 1

    if n_target != 4:
        return False

    for rdx in range(base_rdx, base_rdx+shape[0]):
        for cdx in range(base_cdx, base_cdx+shape[1]):
            board[rdx][cdx] = 0

    return True


def delete_block(board, N):
    counter = 0
    for rdx in range(N):
        for cdx in range(N):
            if possible_to_delete(rdx, cdx, board, N, (2, 3)):
                counter += 1
            elif possible_to_delete(rdx, cdx, board, N, (3, 2)):
                counter += 1
    return counter


def solution(board):
    N = len(board)
    counter = 0
    while True:
        fill_board(board, N)
        cnt = delete_block(board, N)
        if cnt == 0:
            break
        else:
            counter += cnt

    return counter


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
        [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
        [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]
    ]
    assert solution(board) == 2

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 2, 2, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 2

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 1
