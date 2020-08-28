from collections import deque


def bfs(r, c, counter, maps):
    queue = deque([(r, c, counter)])
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    visited = set()
    while queue:
        r, c, counter = queue.popleft()
        visited.add((r, c))

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if nr == len(maps) - 1 and nc == len(maps[0]) - 1:
                return counter + 1

            if (nr, nc) in visited:
                continue
            if not (0 <= nr < len(maps) and 0 <= nc < len(maps[0])):
                continue
            if not maps[nr][nc]:
                continue

            queue.append((nr, nc, counter+1))

    return -1


def solution(maps):
    R = len(maps)
    C = len(maps[0])

    if not (maps[R-1][C-1] or maps[R-1][C-2] or maps[R-2][C-1]):
        return -1

    answer = bfs(0, 0, 1, maps)
    return answer


if __name__ == '__main__':
    maps = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]
    assert solution(maps) == 11
