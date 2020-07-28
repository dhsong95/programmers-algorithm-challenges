import heapq


def solution(food_times, k):
    foods = [(food_time, idx+1) for idx, food_time in enumerate(food_times)]
    heapq.heapify(foods)

    time = 0
    prev_food_time = 0

    while foods:
        cycle = len(foods)
        food_time = foods[0][0]
        time += (cycle * (food_time - prev_food_time))

        if time <= k:
            prev_food_time = food_time
            heapq.heappop(foods)
        else:
            break

    if not foods:
        return -1

    indices = [idx for _, idx in foods]
    indices = sorted(indices)
    return indices[(k-time) % len(indices)]


if __name__ == "__main__":
    assert solution([3, 1, 2], 5) == 1
