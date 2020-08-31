import heapq


def heap_solution(n, cores):
    heap = list()

    for idx in range(len(cores)):
        heapq.heappush(heap, (1, idx))

    while n > 0:
        time, idx = heapq.heappop(heap)
        heapq.heappush(heap, (time+cores[idx], idx))
        n -= 1

    return idx+1


def solution(n, cores):
    answer = heap_solution(n, cores)
    return answer


if __name__ == '__main__':
    assert solution(6, [1, 2, 3]) == 2
