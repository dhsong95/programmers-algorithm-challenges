import sys
sys.setrecursionlimit(100000)


def get_empty_room(room, room_usage):
    if room not in room_usage.keys():
        room_usage[room] = room + 1
        return room

    empty_room = get_empty_room(room_usage[room], room_usage)
    room_usage[room] = empty_room + 1
    return empty_room


def solution(k, room_number):
    rooms = list()
    room_usage = dict()
    for room in room_number:
        empty_room = get_empty_room(room, room_usage)
        rooms.append(empty_room)
    return rooms


if __name__ == '__main__':
    solution(10, [1, 3, 4, 1, 3, 1]) == [1, 3, 4, 2, 5, 6]
