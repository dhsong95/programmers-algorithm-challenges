def solution(msg):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_code = {alphabet: idx+1 for idx, alphabet in enumerate(alphabets)}

    index = 0
    character = ''
    compressed_msg = list()
    while index < len(msg):
        if character + msg[index] in alphabet_code.keys():
            character += msg[index]
        else:
            compressed_msg.append(alphabet_code[character])
            alphabet_code[character + msg[index]] = len(alphabet_code) + 1
            character = msg[index]
        index += 1

    if character:
        compressed_msg.append(alphabet_code[character])

    return compressed_msg


if __name__ == "__main__":
    assert solution('KAKAO') == [11, 1, 27, 15]
    assert solution('TOBEORNOTTOBEORTOBEORNOT') == \
        [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    assert solution('ABABABABABABABAB') == [1, 2, 27, 29, 28, 31, 30]
