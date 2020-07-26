import re


def transform_file(filename):
    filename = filename.lower()
    pattern = r'([^\d]+)([\d]{1,5})(.*)'
    head, number, tail = re.search(pattern, filename).groups()
    return head, number, tail


def solution(files):
    file_info = list()
    for index, filename in enumerate(files):
        head, number, _ = transform_file(filename)
        file_info.append((head, int(number), index))

    return [files[index] for _, _, index in sorted(file_info)]


if __name__ == "__main__":
    files = [
        'img12.png', 'img10.png', 'img02.png',
        'img1.png', 'IMG01.GIF', 'img2.JPG'
    ]
    answer = [
        'img1.png', 'IMG01.GIF', 'img02.png',
        'img2.JPG', 'img10.png', 'img12.png'
    ]
    assert solution(files) == answer

    files = [
        'F-5 Freedom Fighter', 'B-50 Superfortress',
        'A-10 Thunderbolt II', 'F-14 Tomcat'
    ]
    answer = [
        'A-10 Thunderbolt II', 'B-50 Superfortress',
        'F-5 Freedom Fighter', 'F-14 Tomcat'
    ]
    assert solution(files) == answer
