def find_square(m, n, board):
    square = set()
    for idx in range(m-1):
        for jdx in range(n-1):
            target = board[idx][jdx]
            right = board[idx][jdx+1]
            down = board[idx+1][jdx]
            diag = board[idx+1][jdx+1]

            if target and right and down and diag:
                if target == right == down == diag:
                    square.add((idx, jdx))
                    square.add((idx+1, jdx))
                    square.add((idx, jdx+1))
                    square.add((idx+1, jdx+1))

    return square


def remove_square(board, square):
    for idx, jdx in square:
        board[idx][jdx] = None


def reorganize_board(m, n, board):
    for jdx in range(n):
        items = [board[idx][jdx] for idx in range(m) if board[idx][jdx]]
        items = [None] * (m - len(items)) + items
        for idx in range(m):
            board[idx][jdx] = items[idx]


def solution(m, n, board):
    board = [[item for item in row] for row in board]
    counter = 0
    while True:
        square = find_square(m, n, board)
        if len(square) == 0:
            break
        counter += len(square)
        remove_square(board, square)
        reorganize_board(m, n, board)

    return counter


if __name__ == "__main__":
    assert solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']) == 14
    assert solution(6, 6, [
        'TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'
    ]) == 15
