from copy import deepcopy


def rotate(key):
    M = len(key)
    key_rotated = [[0] * M for _ in range(M)]

    for rdx in range(M):
        for cdx in range(M):
            key_rotated[cdx][M-rdx-1] = key[rdx][cdx]

    return key_rotated


def pad_lock(lock, size):
    N = len(lock)
    length = N + (2 * size)
    lock_padded = [[0] * length for _ in range(length)]

    for rdx in range(N):
        for cdx in range(N):
            lock_padded[rdx+size][cdx+size] = lock[rdx][cdx]

    return lock_padded


def unlocked(lock, base, size):
    for rdx in range(base, base+size):
        for cdx in range(base, base+size):
            if lock[rdx][cdx] == 0:
                return False
    return True


def turn_key(key, base_rdx, base_cdx, lock, M, N):
    lock_copy = deepcopy(lock)
    for rdx in range(M):
        for cdx in range(M):
            lock_copy[base_rdx+rdx][base_cdx+cdx] = \
                key[rdx][cdx] ^ lock[base_rdx+rdx][base_cdx+cdx]
    return unlocked(lock_copy, M-1, N)


def solution(key, lock):
    M = len(key)
    N = len(lock)

    lock = pad_lock(lock, M-1)

    for _ in range(4):
        key = rotate(key)

        for rdx in range(M+N-1):
            for cdx in range(M+N-1):
                if turn_key(key, rdx, cdx, lock, M, N):
                    return True

    return False


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert solution(key, lock)
