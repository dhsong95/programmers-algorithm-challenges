def split_two_balanced(p):
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


def transform_balanced_to_valid(p):
    if not p:
        return ''

    valid_parenthesis = ''
    u, v = split_two_balanced(p)
    if is_valid_parenthesis(u):
        valid_parenthesis = u + transform_balanced_to_valid(v)
        return valid_parenthesis
    else:
        valid_parenthesis += '('
        valid_parenthesis += transform_balanced_to_valid(v)
        valid_parenthesis += ')'

        u = u[1:-1]
        u = u.replace('(', '.')
        u = u.replace(')', '(')
        u = u.replace('.', ')')
        valid_parenthesis += u
        return valid_parenthesis


def is_valid_parenthesis(p):
    stack = list()
    for ch in p:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop(-1)
    return not stack


def solution(p):
    valid_parenthesis = transform_balanced_to_valid(p)
    return valid_parenthesis


if __name__ == "__main__":
    assert solution("(()())()") == "(()())()"
    assert solution(")(") == "()"
    assert solution("()))((()") == "()(())()"
