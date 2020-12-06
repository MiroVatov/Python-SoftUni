m = int(input())
n = int(input())
s = int(input())

for num in range(n, m - 1, -1):
    if num % 2 == 0 and num % 3 == 0:
        if num == s:
            break
        else:
            print(f'{num}', end=' ')