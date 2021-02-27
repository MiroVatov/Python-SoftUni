from functools import reduce


def operate(oper, *args):

    if oper == '+':
        return reduce(lambda a, b: a + b, args)

    elif oper == '-':
        return reduce(lambda a, b: a - b, args)

    elif oper == '*':
        return reduce(lambda a, b: a * b, args)

    elif oper == '/':
        return reduce(lambda a, b: a / b, args)


print(operate("*", 10, 3))

