
def math_operations(operator: str, a: int, b: int):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b

    return result


operator = input()
a = int(input())
b = int(input())

print(math_operations(operator, a, b))