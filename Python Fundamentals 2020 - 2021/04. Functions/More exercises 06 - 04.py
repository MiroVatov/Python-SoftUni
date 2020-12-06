num = int(input())
trib_lst = []
number = 0
result = 0
for i in range(1, num + 1):
    trib_lst.append(i)
    result = trib_lst[::3]
    number += result

