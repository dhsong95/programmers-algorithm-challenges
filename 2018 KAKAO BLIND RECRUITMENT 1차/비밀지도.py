

if __name__ == "__main__":
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    assert solution(5, arr1, arr2) == [
        '#####', '# # #', '### #', '#  ##', '#####'
    ]

    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    assert solution(6, arr1, arr2) == [
        '######', '###  #', '##  ##', ' #### ', ' #####', '### # '
    ]
