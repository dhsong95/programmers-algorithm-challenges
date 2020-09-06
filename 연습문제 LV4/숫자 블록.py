def get_max_divisor(n):
    if n == 1:
        return 0

    base = 2
    while base <= (n ** 0.5):
        if (not n % base) and ((n // base) <= 10000000):
            return (n // base)
        base += 1
    return 1


def solution(begin, end):
    answer = list()

    for num in range(begin, end+1):
        max_divisor = get_max_divisor(num)
        answer.append(max_divisor)

    return answer


if __name__ == '__main__':
    assert solution(1, 10) == [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
