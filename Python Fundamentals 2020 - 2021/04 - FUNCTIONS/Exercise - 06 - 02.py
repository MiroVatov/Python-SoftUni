num1 = 0
num2 = 0
num3 = 0

def add_and_subtract(num1, num2, num3):
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    def sum_numbers(num1, num2):
        return num1 + num2

    def subtract(sum_numbers, num3):
        return sum_numbers(num1, num2) - num3
    return subtract(sum_numbers, num3)

print(add_and_subtract(num1, num2, num3))