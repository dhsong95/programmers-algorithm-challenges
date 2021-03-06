import datetime


def transform_to_datetime(line):
    items = line.split()
    duration = float(items[-1][:-1])
    end = datetime.datetime.strptime(
        ' '.join(items[:2]),
        '%Y-%m-%d %H:%M:%S.%f'
    )
    start = end - datetime.timedelta(seconds=(duration - 0.001))
    return (start, end)


def between_one_second(base, start, end):
    if base <= start <= base + datetime.timedelta(seconds=0.999):
        return True
    elif base <= end <= base + datetime.timedelta(seconds=0.999):
        return True
    elif start <= base and base + datetime.timedelta(seconds=0.999) <= end:
        return True
    return False


def solution(lines):
    times = list()
    for line in lines:
        time = transform_to_datetime(line)
        times.append(time)

    counter = 0
    for base_start, base_end in times:
        counter_start = 0
        counter_end = 0

        for start, end in times:
            if between_one_second(base_start, start, end):
                counter_start += 1

            if between_one_second(base_end, start, end):
                counter_end += 1

        counter = max(counter, counter_start, counter_end)

    return counter


if __name__ == '__main__':
    lines = [
        '2016-09-15 20:59:57.421 0.351s',
        '2016-09-15 20:59:58.233 1.181s',
        '2016-09-15 20:59:58.299 0.8s',
        '2016-09-15 20:59:58.688 1.041s',
        '2016-09-15 20:59:59.591 1.412s',
        '2016-09-15 21:00:00.464 1.466s',
        '2016-09-15 21:00:00.741 1.581s',
        '2016-09-15 21:00:00.748 2.31s',
        '2016-09-15 21:00:00.966 0.381s',
        '2016-09-15 21:00:02.066 2.62s'
    ]

    assert solution(lines) == 7
