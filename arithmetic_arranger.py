def arithmetic_arranger(problems, resprint=False):
    upper_operand = ''
    lower_operand = ''
    lines = ''
    res = ''
    for problem in problems:
      single = problem.split()
      first = single[0]
      second = single[2]
      operator = single[1]
      # Defines conditional that cause an error.
      if len(problems) >=6:
        return "Error: Too many problems."
      if (len(first) > 4 or len(second) > 4):
        return "Error: Numbers cannot be more than four digits."
      if operator == '/' or operator == '*':
        return "Error: Operator must be '+' or '-'."
      if not first.isnumeric() or not second.isnumeric():
        return "Error: Numbers must only contain digits."
      # Initialize inplementing.
      if operator == '+' or operator == '-':
        if operator == '+':
          sum = str(int(first) + int(second))
        else:
          sum = str(int(first) - int(second))
        # Displaying formatting section.
        length = max(len(first),len(second)) + 2
        top = first.rjust(length)
        bottom = operator + second.rjust(length-1)
        line = ''
        sumx = sum.rjust(length)
        for l in range(len(top)):
          line += '-'
        # Defines condition whether it is the last one or not.
        if problem != problems[-1]:
          upper_operand += top + '    '
          lower_operand += bottom + '    '
          lines += line + '    '
          res += sumx + '    '
        else:
          upper_operand += top
          lower_operand += bottom
          lines += line
          res += sumx
    if resprint:
      return upper_operand + '\n' + lower_operand + '\n' + lines + '\n' + res
    else:
      return upper_operand + '\n' + lower_operand + '\n' + lines
