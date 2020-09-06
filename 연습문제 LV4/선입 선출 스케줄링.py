import heapq
import math
import random


def heap_solution(n, cores):
    heap = list()

    for idx in range(len(cores)):
        heapq.heappush(heap, (1, idx))

    while n > 0:
        time, idx = heapq.heappop(heap)
        heapq.heappush(heap, (time+cores[idx], idx))
        n -= 1

    return idx+1


def parametric_search_solution(n, cores):
    num_cores = len(cores)
    base = math.ceil((n - num_cores) / num_cores)
    mintime = base * min(cores)
    maxtime = base * max(cores)

    while mintime <= maxtime:
        midtime = (mintime + maxtime) // 2

        counter = len(cores)
        for core in cores:
            counter += (midtime // core)

        if counter < n:
            mintime = midtime + 1
        elif counter >= n:
            maxtime = midtime - 1

    time = mintime
    counter = 0
    for core in cores:
        counter += math.ceil(time / core)

    for idx, core in enumerate(cores):
        counter += int(not time % core)
        if counter == n:
            answer = idx + 1
            break

    return answer


def solution(n, cores):
    answer_heap = heap_solution(n, cores)
    answer_ps = parametric_search_solution(n, cores)

    assert answer_ps == answer_heap
    return answer_ps


if __name__ == '__main__':
    assert solution(6, [1, 2, 3]) == 2

    for _ in range(500):
        n = random.randint(1, 100)
        size = random.randint(1, 5)
        cores = list()
        for _ in range(size):
            cores.append(random.randint(1, 5))

        print(f'{n}\t{cores}')
        solution(n, cores)
