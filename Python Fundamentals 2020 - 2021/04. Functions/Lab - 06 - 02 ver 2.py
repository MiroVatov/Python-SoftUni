
def math_operations(operator: str, a: int, b: int):

    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


operator = input()
a = int(input())
b = int(input())

print(math_operations(operator, a, b))