def move_coord(x, y, arrow):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    return (x+dx[arrow], y+dy[arrow])


def solution(arrows):
    counter = 0
    x, y = (0, 0)
    visited = {(x, y)}
    directions = set()

    for arrow in arrows:
        for _ in range(2):
            nx, ny = move_coord(x, y, arrow)
            if (nx, ny) in visited:
                if not (nx, ny, x, y) in directions and\
                        not (x, y, nx, ny) in directions:
                    counter += 1
            direction = (x, y, nx, ny)
            directions.add(direction)
            visited.add((nx, ny))
            x, y = nx, ny
    return counter


if __name__ == '__main__':
    arrows = [1, 5, 2, 0, 5, 0, 4, 2, 1]
    assert solution(arrows) == 1
