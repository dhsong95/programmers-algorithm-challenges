from itertools import permutations
import re


def split_expression(expression):
    operands = re.findall(r'[\d]{1,3}', expression)
    operands = [int(num) for num in operands]
    operators = re.findall(r'[\+\*\-]', expression)
    return operands, operators


def solution(expression):
    operands_original, operators_original = split_expression(expression)
    priorities = permutations(['+', '-', '*'], 3)

    answer = 0

    for priority in priorities:
        operands = operands_original.copy()
        operators = operators_original.copy()
        for operator in priority:
            while operator in operators:
                index = operators.index(operator)
                operators.pop(index)
                a = operands.pop(index)
                b = operands.pop(index)
                if operator == '+':
                    c = a + b
                elif operator == '-':
                    c = a - b
                elif operator == '*':
                    c = a * b

                operands.insert(index, c)

        answer = max(answer, abs(operands[0]))

    return answer


if __name__ == "__main__":
    assert solution("100-200*300-500+20") == 60420
    assert solution("50*6-3*2") == 300
