from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)


def dfs(node, graph, visited, delayed, next_prev):
    if visited[node]:
        return

    qualified = True
    for prev in next_prev[node]:
        if not visited[prev]:
            delayed[prev].append(node)
            qualified = False
    if not qualified:
        return

    visited[node] = True

    for item in delayed[node]:
        dfs(item, graph, visited, delayed, next_prev)
    delayed.pop(node)

    for item in graph[node]:
        dfs(item, graph, visited, delayed, next_prev)


def solution(n, path, order):
    graph = defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    next_prev = defaultdict(list)
    for a, b in order:
        next_prev[b].append(a)

    visited = [False] * n
    delayed = defaultdict(list)

    dfs(0, graph, visited, delayed, next_prev)

    counter = visited.count(True)
    return counter == n


if __name__ == "__main__":
    assert solution(
        9,
        [
            [0, 1], [0, 3], [0, 7],
            [8, 1], [3, 6], [1, 2],
            [4, 7], [7, 5]
        ],
        [
            [8, 5], [6, 7], [4, 1]
        ]
    )
    assert solution(
        9,
        [
            [8, 1], [0, 1], [1, 2],
            [0, 7], [4, 7], [0, 3],
            [7, 5], [3, 6]
        ],
        [
            [4, 1], [5, 2]
        ]
    )
    assert not solution(
        9,
        [
            [0, 1], [0, 3], [0, 7],
            [8, 1], [3, 6], [1, 2],
            [4, 7], [7, 5]
        ],
        [
            [4, 1], [8, 7], [6, 5]
        ]
    )
