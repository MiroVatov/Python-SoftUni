import sys

num1 = int(input())
num2 = int(input())
num3 = int(input())
lst = [num1,num2,num3]

def smallest():
    min_number = sys.maxsize
    for i in lst:
        if i <= min_number:
            min_number = i

    return min_number

print(smallest())