from itertools import product
import re


def find_banned_user(user_id, banned_id):
    pattern = '^' + banned_id.replace('*', '.') + '$'
    banned_user = list()
    for user in user_id:
        if re.match(pattern, user):
            banned_user.append(user)

    return banned_user


def solution(user_id, banned_id):
    banned_users = list()
    for banned in banned_id:
        banned_user = find_banned_user(user_id, banned)
        banned_users.append(banned_user)

    valid_candidates = list()
    candidates = product(*banned_users)
    for candidate in candidates:
        candidate_set = set(candidate)
        if len(candidate_set) != len(candidate):
            continue

        if candidate_set not in valid_candidates:
            valid_candidates.append(candidate_set)

    return len(valid_candidates)


if __name__ == '__main__':
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    solution(user_id, banned_id) == 2

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    solution(user_id, banned_id) == 2

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    solution(user_id, banned_id) == 3
