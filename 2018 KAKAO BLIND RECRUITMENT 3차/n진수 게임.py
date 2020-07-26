def decimal_to_nary(number, n):
    if number == 0:
        return '0'

    digit = '0123456789ABCDEF'
    nary = ''

    while True:
        q = number // n
        r = number % n

        nary += digit[r]

        if q < n:
            if q != 0:
                nary += digit[q]
            break

        number = q

    return nary[::-1]


def solution(n, t, m, p):
    number = 0
    turn = 1
    answer = ''

    while len(answer) < t:
        number_nary = decimal_to_nary(number, n)
        for digit in number_nary:
            if turn == p:
                answer += digit

            if len(answer) == t:
                break

            turn = turn + 1 if turn < m else 1
        number += 1

    return answer


if __name__ == "__main__":
    assert solution(2, 4, 2, 1) == '0111'
    assert solution(16, 16, 2, 1) == '02468ACE11111111'
    assert solution(16, 16, 2, 2) == '13579BDF01234567'
