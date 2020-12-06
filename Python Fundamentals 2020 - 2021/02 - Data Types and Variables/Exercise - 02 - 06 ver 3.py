n = int(input())

for a in range(97, 97 + n):
    for b in range(97, 97 + n):
            for c in range(97, 97 + n):
                print(f'{chr(a)}{chr(b)}{chr(c)}')



