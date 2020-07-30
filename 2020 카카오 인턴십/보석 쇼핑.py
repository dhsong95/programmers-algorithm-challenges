from collections import defaultdict


def solution(gems):
    N = len(set(gems))
    gem_counter = defaultdict(int)

    ldx = 0
    rdx = 0
    result = [1, len(gems)]
    distance = len(gems) - 1
    gem_counter[gems[0]] = 1

    while ldx < len(gems) and rdx < len(gems):
        if len(gem_counter) == N:
            if max(0, rdx - ldx) < distance:
                result = [ldx+1, rdx+1]
                distance = max(0, rdx - ldx)
            gem_counter[gems[ldx]] -= 1
            if gem_counter[gems[ldx]] == 0:
                gem_counter.pop(gems[ldx])
            ldx += 1
        else:
            rdx += 1
            if rdx < len(gems):
                gem_counter[gems[rdx]] += 1
    return result


if __name__ == "__main__":
    assert solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    ) == [3, 7]
    assert solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3]
    assert solution(["XYZ", "XYZ", "XYZ"]) == [1, 1]
    assert solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5]
