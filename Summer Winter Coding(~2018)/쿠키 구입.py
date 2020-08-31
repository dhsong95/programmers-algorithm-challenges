import sys


def solution(cookie):
    answer = 0
    N = len(cookie)

    for idx in range(N-1):
        front_idx = idx
        front_value = cookie[front_idx]

        rear_idx = idx + 1
        rear_value = cookie[rear_idx]

        while True:
            if front_value == rear_value:
                answer = max(answer, front_value)

            if front_idx > 0 and front_value <= rear_value:
                front_idx -= 1
                front_value += cookie[front_idx]
            elif rear_idx < N-1 and front_value >= rear_value:
                rear_idx += 1
                rear_value += cookie[rear_idx]
            else:
                break
    return answer


if __name__ == '__main__':
    assert solution([1, 1, 2, 3]) == 3
    assert solution([1, 2, 4, 5]) == 0
