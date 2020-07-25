


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
