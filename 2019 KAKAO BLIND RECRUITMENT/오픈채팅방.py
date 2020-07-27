def solution(record):
    logs = list()
    user_info = dict()
    for r in record:
        log_info = r.split()
        if log_info[0].lower() in ['enter', 'leave']:
            logs.append((log_info[1], log_info[0]))
        if len(log_info) == 3:
            user_info[log_info[1]] = log_info[2]

    result = list()
    for user_id, operation in logs:
        log_str = user_info[user_id] + '님이 '
        log_str += ('들어왔습니다.' if operation.lower() == 'enter' else '나갔습니다.')
        result.append(log_str)

    return result


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
