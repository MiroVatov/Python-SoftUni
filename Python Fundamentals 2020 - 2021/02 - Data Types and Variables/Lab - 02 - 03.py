num = int(input())
first_num = 0
second_num = 0
for a in range(1, num + 1):
    if len(str(a)) > 1:
        first_num = a // 10
        second_num = a % 10
        res = first_num + second_num
        if res == 5 or res == 7 or res == 11:
            print(f'{a} -> True')
        else:
            print(f'{a} -> False')
    else:
        if a == 5 or a == 7:
            print(f'{a} -> True')
        else:
            print(f'{a} -> False')