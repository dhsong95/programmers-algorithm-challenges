def is_valid(p):
    stack = list()
    for ch in p:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop(-1)
            else:
                return False
    if stack:
        return False
    return True


def split_balanced(p):
    counter_open = 0
    counter_close = 0

    for idx, ch in enumerate(p):
        if ch == '(':
            counter_open += 1
        elif ch == ')':
            counter_close += 1

        if counter_open == counter_close:
            break

    return p[:idx+1], p[idx+1:]


def balanced_to_valid(p):
    if not p:
        return p

    u, v = split_balanced(p)
    if is_valid(u):
        valid_v = balanced_to_valid(v)
        return u + valid_v
    else:
        valid_p = '('
        valid_v = balanced_to_valid(v)
        valid_p += valid_v
        valid_p += ')'

        valid_u = u[1:-1]
        valid_u = valid_u.replace('(', '.')
        valid_u = valid_u.replace(')', '(')
        valid_u = valid_u.replace('.', ')')

        valid_p += valid_u

        return valid_p


def solution(p):
    valid_p = balanced_to_valid(p)
    return valid_p


if __name__ == "__main__":
    assert solution("(()())()") == "(()())()"
    assert solution(")(") == "()"
    assert solution("()))((()") == "()(())()"
