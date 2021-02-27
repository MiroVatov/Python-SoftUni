from functools import reduce


def operate(op, *args):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    return reduce(ops[op], args)


print(operate("*", 3, 4))