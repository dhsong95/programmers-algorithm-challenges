def possible_to_cross(stones, k, n):
    jump = 0
    for stone in stones:
        if stone < n:
            jump += 1
        else:
            jump = 0

        if jump >= k:
            return False
    return True


def solution(stones, k):
    left = min(stones)
    right = max(stones)

    while left < right:
        middle = (left + right) // 2
        if possible_to_cross(stones, k, middle):
            left = middle + 1
        else:
            right = middle - 1

    return right


if __name__ == '__main__':
    assert solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3