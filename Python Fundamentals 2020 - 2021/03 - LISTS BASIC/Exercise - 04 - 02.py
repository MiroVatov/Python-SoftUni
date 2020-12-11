factor = int(input())
count = int(input())
lst = []

for i in range(1, count + 1):

    num = i * factor
    lst.append(num)

print(lst)