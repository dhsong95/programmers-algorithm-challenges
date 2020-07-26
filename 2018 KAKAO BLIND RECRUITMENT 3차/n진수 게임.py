def nubmer_to_nary(number, n):
    digits = '0123456789ABCDEF'

    if number == 0:
        return digits[0]

    nary = ''

    while True:
        q = number // n
        r = number % n

        nary += str(digits[r])

        if q < n:
            if q != 0:
                nary += str(digits[q])
            break

        number = q

    return nary[::-1]


def solution(n, t, m, p):
    turn = 1
    number = 0
    answer = ''

    while len(answer) < t:
        number_nary = nubmer_to_nary(number, n)
        for index in range(len(number_nary)):
            if turn == p:
                answer += number_nary[index]

            if len(answer) == t:
                break

            turn = turn + 1 if turn < m else 1
        number += 1

    return answer


if __name__ == "__main__":
    assert solution(2, 4, 2, 1) == '0111'
    assert solution(16, 16, 2, 1) == '02468ACE11111111'
    assert solution(16, 16, 2, 2) == '13579BDF01234567'
