from itertools import permutations


def get_weak_combination(n, weak):
    combination = list()
    for idx in range(len(weak)):
        w = weak[idx:] + [w+n for w in weak[:idx]]
        combination.append(w)

    return combination


def get_dist_combination(dist, size):
    return permutations(dist, size)


def possible_to_fix(weak, dist):
    weak_index = 0
    dist_index = 0

    while dist_index < len(dist) and weak_index < len(weak):
        target = weak[weak_index] + dist[dist_index]

        while (weak_index < len(weak)-1) and (weak[weak_index+1] <= target):
            weak_index += 1
        dist_index += 1
        weak_index += 1

    return weak_index == len(weak)


def fix_weak(weak_combination, dist_combination):
    for dist in dist_combination:
        for weak in weak_combination:
            if possible_to_fix(weak, dist):
                return True
    return False


def solution(n, weak, dist):
    weak_combination = get_weak_combination(n, weak)
    for size in range(1, len(dist) + 1):
        dist_combination = get_dist_combination(dist, size)
        if fix_weak(weak_combination, dist_combination):
            return size
    return -1


if __name__ == "__main__":
    assert solution(12, [1, 5, 6, 10], [1, 2, 3, 4]) == 2
    assert solution(12, [1, 3, 4, 9, 10], [3, 5, 7]) == 1
