def solution(s):
    result = len(s)
    for length in range(1, (len(s)//2)+1):
        compressed = ''
        token = ''
        counter = 1
        for idx in range(0, len(s), length):
            if not token:
                token = s[idx:idx+length]
                continue

            if s[idx:idx+length] == token:
                counter += 1
            else:
                if counter >= 2:
                    compressed += (str(counter) + token)
                else:
                    compressed += token
                token = s[idx:idx+length]
                counter = 1

        if counter >= 2:
            compressed += (str(counter) + token)
        else:
            compressed += token

        result = len(compressed) if len(compressed) < result else result

    return result


if __name__ == "__main__":
    assert solution("aabbaccc") == 7
    assert solution("ababcdcdababcdcd") == 9
    assert solution("abcabcdede") == 8
    assert solution("abcabcabcabcdededededede") == 14
    assert solution("xababcdcdababcdcd") == 17
