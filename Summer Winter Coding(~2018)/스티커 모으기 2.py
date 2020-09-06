def solution(sticker):
    N = len(sticker)
    dp_included = [0] * N
    dp_excluded = [0] * N

    if len(sticker) == 1:
        return sticker[0]

    dp_included[0] = sticker[0]
    dp_included[1] = sticker[0]

    dp_excluded[1] = sticker[1]

    for idx in range(2, N-1):
        dp_included[idx] =\
            max(dp_included[idx-2] + sticker[idx], dp_included[idx-1])
    for idx in range(2, N):
        dp_excluded[idx] =\
            max(dp_excluded[idx-2] + sticker[idx], dp_excluded[idx-1])

    return max(max(dp_included), max(dp_excluded))


if __name__ == '__main__':
    assert solution([14, 6, 5, 11, 3, 9, 2, 10]) == 36
    assert solution([1, 3, 2, 5, 4]) == 8
