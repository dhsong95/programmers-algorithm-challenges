import sys


def solution(strs, t):
    N = len(t)
    words = set(strs)

    dp = {idx: sys.maxsize for idx in range(len(t))}

    for idx in range(N-1, -1, -1):
        target = t[idx:]
        for length in range(1, 6):
            sub_target = target[:length]
            if sub_target in words:
                dp[idx] = min(dp.get(idx), 1 + dp.get(idx+length, 0))

    return dp[0] if dp[0] != sys.maxsize else -1


if __name__ == '__main__':
    strs = ['ba', 'na', 'n', 'a']
    t = 'banana'
    assert solution(strs, t) == 3

    strs = ['app', 'ap', 'p', 'l', 'e', 'ple', 'pp']
    t = 'apple'
    assert solution(strs, t) == 2

    strs = ['ba', 'an', 'nan', 'ban', 'n']
    t = 'banana'
    assert solution(strs, t) == -1
