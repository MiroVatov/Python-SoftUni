import operator


def math_ops(operation):
    n1, sign, n2 = operation.split()
    op = {
        '/': operator.truediv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub,
        '^': operator.pow,
    }[sign]
    return op, float(n1), int(n2)


def exec(op, n1, n2):
    return op(n1, n2)
