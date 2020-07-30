from itertools import permutations


def get_weak_combination(n, weak):
    combinations = list()
    for idx in range(len(weak)):
        combination = weak[idx:] + [w+n for w in weak[:idx]]
        combinations.append(combination)

    return combinations


def get_friend_combination(dist, size):
    return permutations(dist, size)


def total_fix(weak, dist):
    weak_index = 0
    dist_index = 0

    while weak_index < len(weak) and dist_index < len(dist):
        coverage = weak[weak_index] + dist[dist_index]

        while weak_index < len(weak)-1 and coverage >= weak[weak_index+1]:
            weak_index += 1

        dist_index += 1
        weak_index += 1

    return weak_index >= len(weak)


def fix_weak(weak_combination, friend_combination):
    for dist in friend_combination:
        for weak in weak_combination:
            if total_fix(weak, dist):
                return True
    return False


def solution(n, weak, dist):
    weak_combination = get_weak_combination(n, weak)
    for size in range(1, len(dist)+1):
        friend_combination = get_friend_combination(dist, size)
        if fix_weak(weak_combination, friend_combination):
            return size
    return -1


if __name__ == "__main__":
    assert solution(12, [1, 5, 6, 10], [1, 2, 3, 4]) == 2
    assert solution(12, [1, 3, 4, 9, 10], [3, 5, 7]) == 1
