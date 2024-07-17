def arithmetic_arranger(problems, show_answers=False):
    # 1. Check for the number of problems given to the function.
    if len(problems) > 5:
        return "Error: Too many problems."

    # 2. Define the lists to hold the formatted results.
    left_operands = []
    right_operands = []
    operators = []
    answers = []
    widths = []

    # 3. Check if only + or - operators are used.
    split_parts = [problem.split() for problem in problems]
    for parts in split_parts:
        operand1, operator, operand2 = parts
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # 4. Check if only digits are used.
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # 5. Check if each operand has a max of four digits.
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # 6. Define the width between each problem.
        width = max(len(operand1),
                    len(operand2)) + 2  # +2 for the operator and space.
        widths.append(width)

        # 7. Combine the formatted results together.
        left_operands.append(operand1.rjust(width))
        right_operands.append(operator + ' ' + operand2.rjust(width - 2))
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers.append(answer.rjust(width))

    # 8. Combine the formatted results and define them into lines.
    problems = '    '.join(left_operands) + '\n' \
               + '    '.join(right_operands) + '\n' \
               + '    '.join('-' * width for width in widths)

    if show_answers:
        problems += '\n' + '    '.join(answers)

    return problems


print( f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
