from collections import defaultdict


def solution(gems):
    N = len(set(gems))
    gem_shopping = defaultdict(int)

    ldx = rdx = 0
    answer = [1, len(gems)]
    gem_shopping[gems[0]] = 1

    while ldx < len(gems) and rdx < len(gems):
        if len(gem_shopping) == N:
            if (rdx - ldx) < (answer[1] - answer[0]):
                answer = [ldx+1, rdx+1]

            gem_shopping[gems[ldx]] -= 1
            if not gem_shopping[gems[ldx]]:
                gem_shopping.pop(gems[ldx])

            ldx += 1
            if ldx > rdx:
                rdx = ldx
        else:
            rdx += 1
            if rdx < len(gems):
                gem_shopping[gems[rdx]] += 1

    return answer


if __name__ == "__main__":
    assert solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    ) == [3, 7]
    assert solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3]
    assert solution(["XYZ", "XYZ", "XYZ"]) == [1, 1]
    assert solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5]
