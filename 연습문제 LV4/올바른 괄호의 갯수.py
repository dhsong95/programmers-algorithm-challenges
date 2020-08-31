from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


def count_valid_parenthesis(p, closed, n):
    if len(p) == (2*n):
        return int(closed == 0)

    counter = 0
    if not closed:
        counter += count_valid_parenthesis(p+'(', closed+1, n)
    else:
        counter += count_valid_parenthesis(p+'(', closed+1, n)
        counter += count_valid_parenthesis(p+')', closed-1, n)

    return counter


def factorial(n, memoization):
    if n in memoization:
        return memoization[n]

    memoization[n] = n * factorial(n-1, memoization)
    return memoization[n]


def catalan_number(n):
    memoization = defaultdict(int)
    memoization[0] = 1
    memoization[1] = 1

    return factorial(2*n, memoization) /\
        (factorial(n+1, memoization) * factorial(n, memoization))


def solution(n):
    counter = count_valid_parenthesis('', 0, n)
    counter_catalan = catalan_number(n)
    assert counter == counter_catalan
    return counter


if __name__ == '__main__':
    solution(4)
