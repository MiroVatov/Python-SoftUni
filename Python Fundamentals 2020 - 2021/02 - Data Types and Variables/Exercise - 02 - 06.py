n = int(input())
begin = 97
for a in range(97, begin + n):
    if a <= (97 + (n - 1)):
        for b in range(97, begin + n):
            if b <= (97 + (n - 1)):
                for c in range(97, begin + n):
                    if c <= (97 + (n - 1)):
                        print(f'{chr(a)}{chr(b)}{chr(c)}')

