from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


def dfs(current, graph, precedents, delayed, visited):
    if visited[current]:
        return

    if (current in precedents) and (not visited[precedents[current]]):
        delayed[precedents[current]].append(current)
        return

    visited[current] = True

    for node in delayed[current]:
        dfs(node, graph, precedents, delayed, visited)
    delayed.pop(current)

    for node in graph[current]:
        dfs(node, graph, precedents, delayed, visited)


def solution(n, path, order):
    graph = defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    precedents = defaultdict()
    for a, b in order:
        precedents[b] = a

    visited = [False] * n
    delayed = defaultdict(list)
    dfs(0, graph, precedents, delayed, visited)

    return visited.count(True) == n


if __name__ == "__main__":
    n = 9
    path = [[0, 1], [0, 3], [0, 7],
            [8, 1], [3, 6], [1, 2],
            [4, 7], [7, 5]]
    order = [[8, 5], [6, 7], [4, 1]]
    assert solution(n, path, order)

    n = 9
    path = [[8, 1], [0, 1], [1, 2],
            [0, 7], [4, 7], [0, 3],
            [7, 5], [3, 6]]
    order = [[4, 1], [5, 2]]
    assert solution(n, path, order)

    n = 9
    path = [[0, 1], [0, 3], [0, 7],
            [8, 1], [3, 6], [1, 2],
            [4, 7], [7, 5]]
    order = [[4, 1], [8, 7], [6, 5]]
    assert not solution(n, path, order)
