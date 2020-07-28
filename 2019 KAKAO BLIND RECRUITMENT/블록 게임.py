def fill_board(board):
    N = len(board)

    for cdx in range(N):
        for rdx in range(N):
            if board[rdx][cdx] <= 0:
                board[rdx][cdx] = -1
            else:
                break


def get_target_block(base_rdx, base_cdx, board, shape):
    target = board[base_rdx][base_cdx]
    if target > 0:
        return target

    for rdx in range(base_rdx, base_rdx+shape[0]):
        for cdx in range(base_cdx, base_cdx+shape[1]):
            if board[rdx][cdx] > 0:
                target = board[rdx][cdx]
                return target

    return target


def possible_to_delete(base_rdx, base_cdx, board, shape):
    N = len(board)
    if base_rdx + shape[0] > N or base_cdx + shape[1] > N:
        return False

    target = get_target_block(base_rdx, base_cdx, board, shape)
    # Only 0 or -1
    if target <= 0:
        return False

    counter = 0
    for rdx in range(base_rdx, base_rdx+shape[0]):
        for cdx in range(base_cdx, base_cdx+shape[1]):
            if board[rdx][cdx] == 0:
                return False

            if board[rdx][cdx] == target:
                counter += 1
            elif board[rdx][cdx] > 0 and board[rdx][cdx] != target:
                return False

    if counter != 4:
        return False

    for rdx in range(base_rdx, base_rdx+shape[0]):
        for cdx in range(base_cdx, base_cdx+shape[1]):
            if board[rdx][cdx] == target:
                board[rdx][cdx] = 0

    return counter


def delete_block(board):
    N = len(board)
    counter = 0
    for rdx in range(N):
        for cdx in range(N):
            if possible_to_delete(rdx, cdx, board, (2, 3)):
                counter += 1
            elif possible_to_delete(rdx, cdx, board, (3, 2)):
                counter += 1

    return counter


def solution(board):
    counter = 0
    while True:
        fill_board(board)
        deleted = delete_block(board)
        if deleted == 0:
            break
        counter += deleted

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
