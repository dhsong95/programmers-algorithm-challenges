def get_gcd(W, H):
    if not H:
        return W
    return get_gcd(H, W % H)


def solution(W, H):
    W, H = max(W, H), min(W, H)
    gcd = get_gcd(W, H)

    W_remain = W // gcd
    H_remain = H // gcd

    return (W * H) - gcd * (W_remain + H_remain - 1)


if __name__ == "__main__":
    assert solution(8, 12) == 80
