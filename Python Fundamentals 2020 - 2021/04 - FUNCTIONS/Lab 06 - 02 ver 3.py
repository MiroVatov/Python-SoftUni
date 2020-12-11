import operator

operators = input()
a = int(input())
b = int(input())

def math_operations(operators: str, a: int, b: int):
    operator_fn = None

    if operators == 'multiply':
        operator_fn = operator.mul
    elif operators == 'divide':
        operator_fn = operator.truediv
    elif operators == 'add':
        operator_fn = operator.add
    elif operators == 'subtract':
        operator_fn = operator.sub

    return operator_fn(a, b)



print(int(math_operations(operators, a, b)))