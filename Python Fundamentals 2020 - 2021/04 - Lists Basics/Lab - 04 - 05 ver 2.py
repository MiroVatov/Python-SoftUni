n = int(input())
lst = []
filtered_lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

command = input()

if command == 'even':
    for num1 in lst:
        if num1 % 2 == 0:
            filtered_lst.append(num1)
    print(filtered_lst)

elif command == 'odd':
    for num1 in lst:
        if num1 % 2 != 0:
            filtered_lst.append(num1)
    print(filtered_lst)

elif command == 'positive':
    for num1 in lst:
        if num1 >= 0:
            filtered_lst.append(num1)
    print(filtered_lst)

elif command == 'negative':
    for num1 in lst:
        if num1 < 0:
            filtered_lst.append(num1)
    print(filtered_lst)