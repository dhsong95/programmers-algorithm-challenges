def replace_chord_sharp(melody):
    for chord in 'ABCDEFG':
        chord_sharp = chord + '#'
        melody = melody.replace(chord_sharp, chord.lower())
    return melody


def get_musicinfo(musicinfo):
    start, end, title, melody = musicinfo.split(',')
    melody = replace_chord_sharp(melody)
    return start, end, title, melody


def get_duration(start, end):
    start = [int(t) for t in start.split(':')]
    end = [int(t) for t in end.split(':')]

    return (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])


def repeat_melody(melody, duration):
    q = duration // len(melody)
    r = duration % len(melody)

    return melody * q + melody[:r]


def solution(m, musicinfo):
    m = replace_chord_sharp(m)
    target_title = '(None)'
    target_duration = 0

    for music in musicinfo:
        start, end, title, melody = get_musicinfo(music)
        duration = get_duration(start, end)
        melody = repeat_melody(melody, duration)

        index = melody.find(m)
        if index >= 0 and target_duration < duration:
            target_title = title
            target_duration = duration

    return target_title


if __name__ == "__main__":
    m = 'ABCDEFG'
    musicinfo = [
        '12:00,12:14,HELLO,CDEFGAB',
        '13:00,13:05,WORLD,ABCDEF'
    ]
    assert solution(m, musicinfo) == 'HELLO'

    m = 'CC#BCC#BCC#BCC#B'
    musicinfo = [
        '03:00,03:30,FOO,CC#B',
        '04:00,04:08,BAR,CC#BCC#BCC#B'
    ]
    assert solution(m, musicinfo) == 'FOO'

    m = 'ABC'
    musicinfo = [
        '12:00,12:14,HELLO,C#DEFGAB',
        '13:00,13:05,WORLD,ABCDEF'
    ]
    assert solution(m, musicinfo) == 'WORLD'

    m = 'CC'
    musicinfo = [
        "04:00,04:02,ZERO,B#CC",
        "15:00,15:02,FIRST,B#CC",
        "04:04,04:06,SECOND,B#CC",
        "04:08,04:10,THIRD,B#CC"
    ]
    assert solution(m, musicinfo) == "(None)"
