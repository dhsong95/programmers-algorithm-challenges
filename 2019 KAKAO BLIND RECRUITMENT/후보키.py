def check_uniqueness(column_indices, relation):
    n_row = len(relation)

    new_rows = set()
    for row in relation:
        new_row = ''
        for cdx in column_indices:
            new_row += row[cdx]
        new_rows.add(new_row)

    if len(new_rows) == n_row:
        return True
    else:
        return False


def solution(relation):
    R = len(relation)
    C = len(relation[0])

    candidates = list()
    for num in range(1, int('1'*C, 2)+1):
        combination_bit = bin(num)[2:]
        combination_bit = '0'*(C-len(combination_bit)) + combination_bit
        column_indices = set([
            idx for idx, bit in enumerate(combination_bit) if bit == '1'
        ])

        if check_uniqueness(column_indices, relation):
            candidates.append(column_indices)

    n_candidate = len(candidates)
    deleted_candidates = list()
    for idx in range(n_candidate):
        for jdx in range(n_candidate):
            if idx == jdx:
                continue
            if candidates[idx].issubset(candidates[jdx]):
                if candidates[jdx] not in deleted_candidates:
                    deleted_candidates.append(candidates[jdx])

    return len(candidates) - len(deleted_candidates)


if __name__ == "__main__":
    relation = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]
    assert solution(relation) == 2
