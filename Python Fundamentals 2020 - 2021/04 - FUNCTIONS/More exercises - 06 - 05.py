def multiplication_sign(num1, num2, num3):
    result = ''

    if num1 == 0 or num2 == 0 or num3 == 0:
        result = "zero"
    elif num1 > 0 and num2 > 0 and num3 > 0:
        result = "positive"
    elif num1 < 0 and num2 < 0 and num3 > 0:
        result = "positive"
    elif num1 > 0 and num2 < 0 and num3 < 0:
        result = "positive"
    elif num1 < 0 and num2 > 0 and num3 < 0:
        result = "positive"
    elif num1 > 0 and num2 < 0 and num3 > 0:
        result = "negative"
    elif num1 < 0 or num2 < 0 or num3 < 0:
        result = "negative"
    return result

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(multiplication_sign(n1, n2, n3))
