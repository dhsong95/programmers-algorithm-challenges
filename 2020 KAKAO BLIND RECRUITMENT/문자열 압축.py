def solution(s):
    length = len(s)
    for size in range(1, len(s)//2+1):
        compressed = ''
        target = ''
        counter = 1
        for idx in range(0, len(s), size):
            token = s[idx:idx+size]

            if not target:
                target = token
                continue

            if token == target:
                counter += 1
            else:
                if counter >= 2:
                    compressed += (str(counter) + target)
                else:
                    compressed += target
                target = token
                counter = 1

        if counter >= 2:
            compressed += (str(counter) + target)
        else:
            compressed += target

        length = min(length, len(compressed))
    return length

if __name__ == "__main__":
    assert solution("aabbaccc") == 7
    assert solution("ababcdcdababcdcd") == 9
    assert solution("abcabcdede") == 8
    assert solution("abcabcabcabcdededededede") == 14
    assert solution("xababcdcdababcdcd") == 17
