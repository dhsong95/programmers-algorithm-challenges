def get_distance(current, target):
    left = ['1', '4', '7', '*']
    right = ['3', '6', '9', '#']
    center = ['2', '5', '8', '0']

    distance = 0
    if current in left:
        distance += 1
        current = center[left.index(current)]
    elif current in right:
        distance += 1
        current = center[right.index(current)]

    distance += abs(center.index(target) - center.index(current))

    return distance


def get_left_or_right(left, right, target, hand):
    if target in ['1', '4', '7', '*']:
        return 'L'
    elif target in ['3', '6', '9', '#']:
        return 'R'
    else:
        l_distance = get_distance(left, target)
        r_distance = get_distance(right, target)

        if l_distance < r_distance:
            return 'L'
        elif l_distance > r_distance:
            return 'R'
        else:
            return 'L' if hand == 'left' else 'R'


def solution(numbers, hand):
    result = ''
    left = '#'
    right = '*'
    for number in numbers:
        target = str(number)
        lr = get_left_or_right(left, right, target, hand)
        result += lr
        if lr == 'L':
            left = target
        elif lr == 'R':
            right = target
    return result


if __name__ == "__main__":
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == \
        "LRLLLRLLRRL"
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == \
        "LRLLRRLLLRR"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == \
        "LLRLLRLLRL"
