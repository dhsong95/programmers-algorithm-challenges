def solution(N, stages):
    not_clear = {stage: 0 for stage in range(1, N+2)}
    play = {stage: 0 for stage in range(1, N+2)}

    for stage in stages:

        for s in range(1, stage+1):
            play[s] += 1

        not_clear[stage] += 1

    failure = list()
    for stage in range(1, N+1):
        failure_rate = not_clear[stage] / play[stage] if play[stage] else 0
        failure.append((-failure_rate, stage))

    return [stage for _, stage in sorted(failure)]


if __name__ == "__main__":
    assert solution(
        5, [2, 1, 2, 6, 2, 4, 3, 3]
    ) == [3, 4, 2, 1, 5]
    assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]
