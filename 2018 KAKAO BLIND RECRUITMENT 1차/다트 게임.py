import re


def solution(dartResult):
    pattern = r'([\d]+)([SDT])([\*#]?)'
    scores = list()
    for score, bonus, option in re.findall(pattern, dartResult):
        score = int(score)
        if bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3

        if option == '*':
            if scores:
                scores[-1] = scores[-1] * 2
            score *= 2
        elif option == '#':
            score *= (-1)

        scores.append(score)

    return sum(scores)


if __name__ == "__main__":
    assert solution('1S2D*3T') == 37
    assert solution('1D2S#10S') == 9
    assert solution('1D2S0T') == 3
    assert solution('1S*2T*3S') == 23
    assert solution('1D#2S*3S') == 5
    assert solution('1T2D3D#') == -4
    assert solution('1D2S3T*') == 59
