import heapq


def normalize_time(time):
    hour, minute = time
    if minute >= 60:
        hour += 1
        minute -= 60
        if hour >= 24 and minute != 0:
            hour -= 24
    elif minute < 0:
        minute += 60
        hour -= 1
        if hour < 0:
            hour += 24

    return (hour, minute)


def time_add_minute(time, minute_delta):
    hour, minute = time
    minute += minute_delta
    hour, minute = normalize_time((hour, minute))

    return (hour, minute)


def transform_time(time):
    hour, minute = time.split(':')
    return (int(hour), int(minute))


def commute(n, t, m, heap):
    bus = (9, 0)
    for _ in range(n-1):
        for _ in range(m):
            if heap and heap[0] <= bus:
                heapq.heappop(heap)
            else:
                break
        bus = time_add_minute(bus, t)

    return bus


def solution(n, t, m, timetable):
    heap = list()
    for time in timetable:
        heapq.heappush(heap, transform_time(time))
    last_bus = commute(n, t, m, heap)

    if heap and len(heap) < m:
        return '{:02d}:{:02d}'.format(last_bus[0], last_bus[1])

    for _ in range(m):
        if heap and heap[0] <= last_bus:
            last_person = heapq.heappop(heap)
        else:
            return '{:02d}:{:02d}'.format(last_bus[0], last_bus[1])

    conn = time_add_minute(last_person, -1)
    return '{:02d}:{:02d}'.format(conn[0], conn[1])


if __name__ == '__main__':
    assert solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']) == '09:00'
    assert solution(2, 10, 2, ['09:10', '09:09', '08:00']) == '09:09'
    assert solution(2, 1, 2, ['09:00', '09:00', '09:00', '09:00']) == '08:59'
    assert solution(1, 1, 5, [
        '00:01', '00:01', '00:01', '00:01', '00:01'
    ]) == '00:00'
    assert solution(1, 1, 1, ['23:59']) == '09:00'
    assert solution(10, 60, 45, [
        '23:59', '23:59', '23:59', '23:59', '23:59',
        '23:59', '23:59', '23:59', '23:59', '23:59',
        '23:59', '23:59', '23:59', '23:59', '23:59', '23:59'
    ]) == '18:00'
