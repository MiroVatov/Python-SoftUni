num1 = 0
num2 = 0
num3 = 0

def add_and_subtract():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    def sum_numbers():
        result1 = num1 + num2
        return result1

    def subtract():
        result2 = sum_numbers() - num3
        return result2

    return subtract()

print(add_and_subtract())