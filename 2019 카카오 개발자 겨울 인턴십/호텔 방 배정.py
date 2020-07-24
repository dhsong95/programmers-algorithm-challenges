import sys
sys.setrecursionlimit(10000000)


def find_empty_room(room, room_dict):
    if room not in room_dict.keys():
        room_dict[room] = room + 1
        return room

    empty_room = find_empty_room(room_dict[room], room_dict)
    room_dict[room] = empty_room + 1
    return empty_room


def solution(k, room_number):
    room_dict = dict()
    rooms = list()

    for room in room_number:
        empty_room = find_empty_room(room, room_dict)
        rooms.append(empty_room)

    return rooms


if __name__ == '__main__':
    solution(10, [1, 3, 4, 1, 3, 1]) == [1, 3, 4, 2, 5, 6]
