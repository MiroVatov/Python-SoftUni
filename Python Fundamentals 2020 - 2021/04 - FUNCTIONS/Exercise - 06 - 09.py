num1 = int(input())
num2 = int(input())


def factoriel(num1, num2):

    for a in range(num1, 1, -1):
        num1 *= a - 1

    for b in range(num2, 1, -1):
        num2 *= b - 1

    result = num1 / num2
    print(f'{result:.2f}')
    return result


factoriel(num1, num2)