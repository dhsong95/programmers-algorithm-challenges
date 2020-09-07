def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[0] * N for _ in range(N)]

    for gap in range(1, N):
        for start in range(N):
            end = start + gap
            if end >= N:
                continue

            for k in range(start, end):
                score = dp[start][k] + dp[k+1][end] +\
                    matrix_sizes[start][0] * matrix_sizes[k][1] *\
                    matrix_sizes[end][1]
                if not dp[start][end]:
                    dp[start][end] = score
                else:
                    dp[start][end] = min(dp[start][end], score)

    return dp[0][-1]


if __name__ == '__main__':
    assert solution([[5, 3], [3, 10], [10, 6]]) == 270
