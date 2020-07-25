def possible_to_cross(n, stones, k):
    counter = 0
    for stone in stones:
        counter = counter + 1 if stone < n else 0
        if counter >= k:
            return False
    return True


def solution(stones, k):
    left = min(stones)
    right = max(stones)

    while left <= right:
        middle = left + ((right - left) // 2)
        possible = possible_to_cross(middle, stones, k)
        if possible:
            left = middle + 1
        else:
            right = middle - 1

    return right


if __name__ == '__main__':
    assert solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3
