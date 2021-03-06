from collections import Counter
import re


def solution(s):
    nums = re.findall(r'[\d]+', s)
    counter = Counter(nums)
    return [int(item[0]) for item in counter.most_common()]


if __name__ == '__main__':
    assert solution('{{2},{2,1},{2,1,3},{2,1,3,4}}') == [2, 1, 3, 4]
    assert solution('{{1,2,3},{2,1},{1,2,4,3},{2}}') == [2, 1, 3, 4]
    assert solution('{{20,111},{111}}') == [111, 20]
    assert solution('{{123}}') == [123]
    assert solution('{{4,2,3},{3},{2,3,4,1},{2,3}}') == [3, 2, 4, 1]
