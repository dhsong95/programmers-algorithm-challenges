def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = list()

    for combination in range(1, int('1' * n_col, 2) + 1):
        combination = bin(combination)[2:]
        combination = '0' * (n_col - len(combination)) + combination
        combination = [
            index for index, bit in enumerate(combination) if bit == '1'
        ]

        new_rows = set()
        for row in relation:
            new_row = ''.join(row[index] for index in combination)
            new_rows.add(new_row)

        if len(new_rows) == n_row:
            candidates.append(combination)

    redundants = list()
    for combination_src in candidates:
        for combination_dst in candidates:
            if set(combination_src) == set(combination_dst):
                continue

            if set(combination_src).issubset(set(combination_dst)):
                if combination_dst not in redundants:
                    redundants.append(combination_dst)

    return len(candidates) - len(redundants)


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
