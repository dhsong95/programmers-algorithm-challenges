def calculate_distance(source, target):
    left_numbers = ['1', '4', '7', '*']
    right_numbers = ['3', '6', '9', '#']
    center_numbers = ['2', '5', '8', '0']

    distance = 0
    if source in left_numbers:
        distance = 1
        source = center_numbers[left_numbers.index(source)]
    elif source in right_numbers:
        distance = 1
        source = center_numbers[right_numbers.index(source)]

    distance +=\
        abs(center_numbers.index(target) - center_numbers.index(source))
    return distance


def press_button(left, right, target, hand):
    left_numbers = ['1', '4', '7', '*']
    right_numbers = ['3', '6', '9', '#']
    center_numbers = ['2', '5', '8', '0']

    if target in left_numbers:
        return 'L'
    elif target in right_numbers:
        return 'R'
    elif target in center_numbers:
        distance_left = calculate_distance(left, target)
        distance_right = calculate_distance(right, target)

        if distance_left < distance_right:
            return 'L'
        elif distance_left > distance_right:
            return 'R'
        else:
            return 'L' if hand == 'left' else 'R'


def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'

    for number in numbers:
        number = str(number)
        direction = press_button(left, right, number, hand)
        answer += direction
        if direction == 'L':
            left = number
        elif direction == 'R':
            right = number

    return answer


if __name__ == "__main__":
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == \
        "LRLLLRLLRRL"
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == \
        "LRLLRRLLLRR"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == \
        "LLRLLRLLRL"
