def update_cache(cache, city, size):
    if size == 0:
        return 5

    if city in cache:
        index = cache.index(city)
        cache.pop(index)
        cache.append(city)
        return 1

    if len(cache) < size:
        cache.append(city)
        return 5
    else:
        cache.pop(0)
        cache.append(city)
        return 5


def solution(cacheSize, cities):
    cache = list()
    time = 0
    for city in cities:
        city = city.lower()
        time += update_cache(cache, city, cacheSize)

    return time


if __name__ == "__main__":
    cities = [
        'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
        'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'
    ]
    assert solution(3, cities) == 50

    cities = [
        'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo',
        'Seoul', 'Jeju', 'Pangyo', 'Seoul'
    ]
    assert solution(3, cities) == 21

    cities = [
        'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
        'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju',
        'NewYork', 'Rome'
    ]
    assert solution(2, cities) == 60

    cities = [
        'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco',
        'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'
    ]
    assert solution(5, cities) == 52

    cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
    assert solution(2, cities) == 16

    cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
    assert solution(0, cities) == 25
