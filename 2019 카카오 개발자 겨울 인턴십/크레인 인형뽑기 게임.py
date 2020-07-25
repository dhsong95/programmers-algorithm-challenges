from collections import deque


def get_item(board, move, N):
    item = 0
    for index in range(N):
        if board[index][move-1] != 0:
            item = board[index][move-1]
            board[index][move-1] = 0
            break
    return item


def solution(board, moves):
    N = len(board)
    stack = deque([])
    counter = 0
    for move in moves:
        item = get_item(board, move, N)
        if item == 0:
            continue

        if stack and stack[-1] == item:
            counter += 2
            stack.pop()
        else:
            stack.append(item)

    return counter


if __name__ == '__main__':
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    assert solution(board, moves) == 4
