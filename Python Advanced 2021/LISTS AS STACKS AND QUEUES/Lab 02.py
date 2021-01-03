expression = input()
stack = []


for char in expression:
    if char == '(':
        stack.append('')

    for index in range(len(stack)):
        stack[index] += char

    if char == ')':
        sub_expression = stack.pop()
        print(sub_expression)