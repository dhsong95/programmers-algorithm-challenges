import sys


def solution(land, P, Q):
    heights = sorted(sum(land, []))
    TOTAL = sum(heights)
    N = len(heights)

    prev = 0
    answer = sys.maxsize
    for idx, height in enumerate(heights):
        base_p = (idx * height - prev)
        base_q = TOTAL - prev - ((N - idx) * height)

        cost = base_p * P + base_q * Q
        if cost > answer:
            break
        else:
            answer = cost

        prev += height

    return answer


if __name__ == '__main__':
    assert solution([[1, 2], [2, 3]], 3, 2) == 5
    assert solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3) == 33
