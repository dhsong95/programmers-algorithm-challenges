from collections import deque
from collections import defaultdict
import random
import sys
sys.setrecursionlimit(10**9)


def in_boundary(rdx, cdx, land_group):
    N = len(land_group)
    return 0 <= rdx < N and 0 <= cdx < N


def already_grouped(rdx, cdx, land_group):
    return land_group[rdx][cdx]


def too_high_to_cross(rdx, cdx, dr, dc, land, height):
    base = land[rdx][cdx]
    return abs(base - land[rdx+dr][cdx+dc]) > height


def in_same_group(rdx, cdx, dr, dc, land_group):
    return land_group[rdx][cdx] == land_group[rdx+dr][cdx+dc]


def dfs(rdx, cdx, group, land_group, land, height):
    delta_row = [0, 0, 1, -1]   # RLDU
    delta_col = [1, -1, 0, 0]   # RLDU

    land_group[rdx][cdx] = group

    for dr, dc in zip(delta_row, delta_col):
        if not in_boundary(rdx+dr, cdx+dc, land_group):
            continue
        if already_grouped(rdx+dr, cdx+dc, land_group):
            continue
        if too_high_to_cross(rdx, cdx, dr, dc, land, height):
            continue

        dfs(rdx+dr, cdx+dc, group, land_group, land, height)


def get_land_group(land, height):
    N = len(land)
    land_group = [[0] * N for _ in range(N)]

    group = 1
    for rdx in range(N):
        for cdx in range(N):
            if land_group[rdx][cdx]:
                continue
            dfs(rdx, cdx, group, land_group, land, height)
            group += 1

    return land_group


def get_graph(land_group, land, height):
    N = len(land_group)

    delta_row = [0, 0, 1, -1]   # RLDU
    delta_col = [1, -1, 0, 0]   # RLDU

    graph = defaultdict(lambda: defaultdict(lambda: sys.maxsize))
    for rdx in range(N):
        for cdx in range(N):
            for dr, dc in zip(delta_row, delta_col):
                if not in_boundary(rdx+dr, cdx+dc, land_group):
                    continue
                if in_same_group(rdx, cdx, dr, dc, land_group):
                    continue
                node_u = land_group[rdx][cdx]
                node_v = land_group[rdx+dr][cdx+dc]
                distance = abs(land[rdx][cdx] - land[rdx+dr][cdx+dc])

                graph[node_u][node_v] = min(graph[node_u][node_v], distance)
                graph[node_v][node_u] = min(graph[node_v][node_u], distance)

    return graph


def get_parent(node, parents):
    while parents[node] != node:
        node = parents[node]
    return node


def kruskal_algorithm(graph):
    graph_set = set()
    for u, v_distance in graph.items():
        for v, distance in v_distance.items():
            node_u, node_v = min(u, v), max(u, v)
            graph_set.add((distance, node_u, node_v))

    graph_set = sorted(graph_set)

    cost = 0
    parents = {node: node for node in graph.keys()}
    visited = set()
    for distance, u, v in graph_set:
        u_parent = get_parent(u, parents)
        v_parent = get_parent(v, parents)

        if u_parent == v_parent:
            continue

        visited.add(u)
        visited.add(v)
        cost += distance
        u_parent, v_parent = min(u_parent, v_parent), max(u_parent, v_parent)
        parents[v_parent] = u_parent

        if parents.values() == [1] * len(parents):
            break

    return cost


def solution(land, height):
    land_group = get_land_group(land, height)

    graph = get_graph(land_group, land, height)

    cost = kruskal_algorithm(graph)

    return cost


if __name__ == "__main__":
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    height = 3
    assert solution(land, height) == 15

    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    assert solution(land, height) == 18

    land = [[2, 1, 4], [7, 7, 7], [8, 5, 8]]
    height = 1
    assert solution(land, height) == 8
