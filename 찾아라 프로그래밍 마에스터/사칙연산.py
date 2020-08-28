from collections import defaultdict
import sys


def get_max(arr, memoization):
    if len(arr) == 1:
        return int(arr[0])

    key = ' '.join(arr) + 'MX'
    if memoization[key]:
        return memoization[key]

    answer = -sys.maxsize
    for idx in range(1, len(arr), 2):
        if arr[idx] == '-':
            candidate =\
                get_max(arr[:idx], memoization) -\
                get_min(arr[idx+1:], memoization)
        elif arr[idx] == '+':
            candidate =\
                get_max(arr[:idx], memoization) +\
                get_max(arr[idx+1:], memoization)
        answer = max(answer, candidate)

    memoization[key] = answer
    return answer


def get_min(arr, memoization):
    if len(arr) == 1:
        return int(arr[0])

    key = ' '.join(arr) + 'MN'
    if memoization[key]:
        return memoization[key]

    answer = sys.maxsize
    for idx in range(1, len(arr), 2):
        if arr[idx] == '-':
            candidate =\
                get_min(arr[:idx], memoization) -\
                get_max(arr[idx+1:], memoization)
        elif arr[idx] == '+':
            candidate = \
                get_min(arr[:idx], memoization) +\
                get_min(arr[idx+1:], memoization)
        answer = min(answer, candidate)

    memoization[key] = answer
    return answer


def solution(arr):
    memoization = defaultdict(int)
    answer = get_max(arr, memoization)
    return answer


if __name__ == '__main__':
    arr = ['1', '-', '3', '+', '5', '-', '8']
    assert solution(arr) == 1

    arr = ['5', '-', '3', '+', '1', '+', '2', '-', '4']
    assert solution(arr) == 3
