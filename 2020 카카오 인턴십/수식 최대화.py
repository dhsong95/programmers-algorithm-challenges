from itertools import permutations
import re


def solution(expression):
    candidates = permutations(['+', '-', '*'], 3)
    operands_original = re.findall(r'[\d]{1,3}', expression)
    operands_original = [int(num) for num in operands_original]
    operators_original = re.findall(r'[\+\-\*]', expression)
    result = 0

    for candidate in candidates:
        operands = operands_original.copy()
        operators = operators_original.copy()

        for operator in candidate:

            if operator not in operators:
                continue

            while operator in operators:
                index = operators.index(operator)
                operators.pop(index)
                a = operands.pop(index)
                b = operands.pop(index)
                if operator == '+':
                    operands.insert(index, a+b)
                elif operator == '-':
                    operands.insert(index, a-b)
                elif operator == '*':
                    operands.insert(index, a*b)

        result = max(result, abs(operands[0]))

    return result


if __name__ == "__main__":
    assert solution("100-200*300-500+20") == 60420
    assert solution("50*6-3*2") == 300
