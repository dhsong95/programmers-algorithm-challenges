from copy import deepcopy


def zero_padding(lock, pad_size):
    n_lock = len(lock)
    size = len(lock) + (2 * pad_size)
    lock_padded = [[0] * size for _ in range(size)]

    for idx in range(n_lock):
        for jdx in range(n_lock):
            lock_padded[idx+pad_size][jdx+pad_size] = lock[idx][jdx]

    return lock_padded


def unlocked(pattern, lock_size, pad_size):
    for idx in range(lock_size):
        for jdx in range(lock_size):
            if pattern[idx+pad_size][jdx+pad_size] == 0:
                return False
    return True


def make_pattern(base_idx, base_jdx, key, lock):
    n_key = len(key)
    pattern = deepcopy(lock)
    for idx in range(n_key):
        for jdx in range(n_key):
            pattern[base_idx+idx][base_jdx+jdx] =\
                lock[base_idx+idx][base_jdx+jdx] ^ key[idx][jdx]

    return pattern


def try_to_unlock(key, lock, n_key, n_lock):
    for idx in range(n_key+n_lock-1):
        for jdx in range(n_key+n_lock-1):
            pattern = make_pattern(idx, jdx, key, lock)
            if unlocked(pattern, n_lock, n_key-1):
                return True
    return False


def rotate_key(key):
    n_key = len(key)
    key_rotated = [[0] * n_key for _ in range(n_key)]

    for idx in range(n_key):
        for jdx in range(n_key):
            key_rotated[idx][jdx] = key[jdx][n_key-idx-1]

    return key_rotated


def solution(key, lock):
    n_key = len(key)
    n_lock = len(lock)

    lock = zero_padding(lock, n_key-1)

    for _ in range(4):
        key = rotate_key(key)
        if try_to_unlock(key, lock, n_key, n_lock):
            return True

    return False


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert solution(key, lock)
