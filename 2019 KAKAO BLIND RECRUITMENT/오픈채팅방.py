def solution(record):
    logs = list()
    nicknames = dict()
    for rec in record:
        rec = rec.split()
        if len(rec) == 3:
            nicknames[rec[1]] = rec[2]
        if rec[0] in ['Enter', 'Leave']:
            log = [rec[1], '님이 들어왔습니다.' if rec[0] == 'Enter' else '님이 나갔습니다.']
            logs.append(log)

    for idx, (user, msg) in enumerate(logs):
        logs[idx] = nicknames[user] + msg

    return logs


if __name__ == "__main__":
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]
    result = [
        "Prodo님이 들어왔습니다.",
        "Ryan님이 들어왔습니다.",
        "Prodo님이 나갔습니다.",
        "Prodo님이 들어왔습니다."
    ]

    assert solution(record) == result
