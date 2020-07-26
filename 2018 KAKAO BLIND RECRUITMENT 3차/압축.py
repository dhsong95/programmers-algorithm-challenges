def solution(msg):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codebook = {ch: idx+1 for idx, ch in enumerate(alphabet)}

    index = 0
    target = ''
    code = list()
    while index < len(msg):
        ch = msg[index]
        if target + ch in codebook:
            target += ch
        else:
            code.append(codebook[target])
            codebook[target+ch] = len(codebook) + 1
            target = ch
        index += 1

    code.append(codebook[target])

    return code


if __name__ == "__main__":
    assert solution('KAKAO') == [11, 1, 27, 15]
    assert solution('TOBEORNOTTOBEORTOBEORNOT') == \
        [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    assert solution('ABABABABABABABAB') == [1, 2, 27, 29, 28, 31, 30]
