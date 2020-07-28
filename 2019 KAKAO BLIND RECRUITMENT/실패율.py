def solution(N, stages):
    stage_try = {stage: 0 for stage in range(1, N+2)}
    stage_fail = {stage: 0 for stage in range(1, N+2)}

    for stage in stages:
        for s in range(1, stage+1):
            stage_try[s] += 1
        stage_fail[stage] += 1

    scores = list()
    for stage in range(1, N+1):
        score = stage_fail[stage] / stage_try[stage]\
            if stage_try[stage] > 0 else 0
        scores.append((-score, stage))

    return [stage for _, stage in sorted(scores)]


if __name__ == "__main__":
    assert solution(
        5, [2, 1, 2, 6, 2, 4, 3, 3]
    ) == [3, 4, 2, 1, 5]
    assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]
