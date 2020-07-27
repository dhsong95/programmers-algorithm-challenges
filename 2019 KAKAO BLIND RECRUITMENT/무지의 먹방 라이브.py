import heapq


def solution(food_times, k):
    foods = [(time, idx+1) for idx, time in enumerate(food_times)]
    heapq.heapify(foods)

    time = 0
    food_time_prev = 0

    while foods:
        cycle = len(foods)
        food_time = foods[0][0]

        time += (food_time - food_time_prev) * cycle

        if time <= k:
            food_time_prev, _ = heapq.heappop(foods)
        else:
            break

    if not foods:
        return -1

    indices = [idx for _, idx in foods]
    indices = sorted(indices)
    return indices[(k-time) % len(indices)]


if __name__ == "__main__":
    assert solution([3, 1, 2], 5) == 1
