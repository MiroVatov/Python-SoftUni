number = int(input())
is_prime = False
delitel = 0
for x in range(1, number + 1):
    if number % x == 0:
        delitel += 1
if delitel == 2:
    is_prime = True

print(f'{is_prime}')