import re


def get_bigram(word):
    word = word.lower()
    bigram = [word[idx:idx+2] for idx in range(len(word)-1) if re.match(
        r'[a-z]{2}', word[idx:idx+2]
    )]
    return bigram


def calculate_jaccard(bigram1, bigram2):
    bigram1 = sorted(bigram1)
    bigram2 = sorted(bigram2)

    idx = 0
    jdx = 0

    n_union = 0
    n_intersect = 0

    while idx < len(bigram1) and jdx < len(bigram2):
        if bigram1[idx] == bigram2[jdx]:
            n_intersect += 1
            idx += 1
            jdx += 1
        elif bigram1[idx] < bigram2[jdx]:
            idx += 1
        elif bigram1[idx] > bigram2[jdx]:
            jdx += 1

        n_union += 1

    n_union += len(bigram1) - idx
    n_union += len(bigram2) - jdx

    score = n_intersect / n_union if n_union > 0 else 1
    return score


def solution(str1, str2):
    bigram1 = get_bigram(str1)
    bigram2 = get_bigram(str2)

    jaccard = calculate_jaccard(bigram1, bigram2)
    return int(jaccard * 65536)


if __name__ == '__main__':
    assert solution('FRANCE', 'french') == 16384
    assert solution('handshake', 'shake hands') == 65536
    assert solution('aa1+aa2', 'AAAA12') == 43690
    assert solution('E=M*C^2', 'e=m*c^2') == 65536
