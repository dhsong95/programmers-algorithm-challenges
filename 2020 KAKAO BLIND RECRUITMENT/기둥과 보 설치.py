def in_boundary(x, y, frames):
    n = len(frames)
    return 0 <= x < n and 0 <= y < n


def valid_frame(pillars, beams):
    n = len(pillars)

    for x in range(n):
        for y in range(n):
            if pillars[x][y] and not valid_pillar(x, y, pillars, beams):
                return False
            if beams[x][y] and not valid_beam(x, y, pillars, beams):
                return False
    return True


def valid_pillar(x, y, pillars, beams):
    if not in_boundary(x, y, pillars):
        return False

    if y == 0:
        return True

    if in_boundary(x, y-1, pillars) and pillars[x][y-1]:
        return True

    if (in_boundary(x, y, beams) and beams[x][y]) or\
            (in_boundary(x-1, y, beams) and beams[x-1][y]):
        return True

    return False


def valid_beam(x, y, pillars, beams):
    if not in_boundary(x, y, beams):
        return False

    if (in_boundary(x-1, y, beams) and beams[x-1][y]) and\
            (in_boundary(x+1, y, beams) and beams[x+1][y]):
        return True

    if (in_boundary(x, y-1, pillars) and pillars[x][y-1]) or\
            (in_boundary(x+1, y-1, pillars) and pillars[x+1][y-1]):
        return True


def construct_pillar(x, y, pillars, beams):
    if valid_pillar(x, y, pillars, beams):
        pillars[x][y] = True


def deconstruct_pillar(x, y, pillars, beams):
    pillars[x][y] = False
    if not valid_frame(pillars, beams):
        pillars[x][y] = True


def construct_beam(x, y, pillars, beams):
    if valid_beam(x, y, pillars, beams):
        beams[x][y] = True


def deconstruct_beam(x, y, pillars, beams):
    beams[x][y] = False
    if not valid_frame(pillars, beams):
        beams[x][y] = True


def solution(n, build_frame):
    pillars = [[False] * (n+1) for _ in range(n+1)]
    beams = [[False] * (n+1) for _ in range(n+1)]

    for x, y, a, b in build_frame:
        if a == 0 and b == 0:
            deconstruct_pillar(x, y, pillars, beams)
        elif a == 0 and b == 1:
            construct_pillar(x, y, pillars, beams)
        elif a == 1 and b == 0:
            deconstruct_beam(x, y, pillars, beams)
        elif a == 1 and b == 1:
            construct_beam(x, y, pillars, beams)

    result = list()
    for x in range(n+1):
        for y in range(n+1):
            if pillars[x][y]:
                result.append([x, y, 0])
            if beams[x][y]:
                result.append([x, y, 1])

    return result


if __name__ == "__main__":
    build_frame = [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 2, 1, 1],
        [5, 0, 0, 1],
        [5, 1, 0, 1],
        [4, 2, 1, 1],
        [3, 2, 1, 1]
    ]
    result = [
        [1, 0, 0],
        [1, 1, 1],
        [2, 1, 0],
        [2, 2, 1],
        [3, 2, 1],
        [4, 2, 1],
        [5, 0, 0],
        [5, 1, 0]
    ]
    assert solution(5, build_frame) == result

    build_frame = [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1]
    ]
    result = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 1, 1],
        [2, 1, 1],
        [3, 1, 1],
        [4, 0, 0]
    ]
    assert solution(5, build_frame) == result
