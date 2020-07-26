def transform_musicinfo(musicinfo):
    start, end, title, melody = musicinfo.split(',')
    return start, end, title, melody


def get_duration(start, end):
    start_hour, start_minute = start.split(':')
    end_hour, end_minute = end.split(':')

    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)

    duration = \
        ((end_hour * 60) + end_minute) - ((start_hour * 60) + start_minute)

    return duration


def repeat_melody(melody, duration):

    q = duration // len(melody)
    r = duration % len(melody)

    return melody * q + melody[:r]


def replace_melody_sharp(melody):
    chords = 'ABCDEFG'
    for chord in chords:
        chord_sharp = chord + '#'
        melody = melody.replace(chord_sharp, chord.lower())

    return melody


def solution(m, musicinfo):
    target_title = '(None)'
    target_duration = 0

    m = replace_melody_sharp(m)

    for music in musicinfo:
        start, end, title, melody = transform_musicinfo(music)
        melody = replace_melody_sharp(melody)
        duration = get_duration(start, end)
        melody = repeat_melody(melody, duration)

        index = melody.find(m)
        if index != -1 and duration > target_duration:
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
