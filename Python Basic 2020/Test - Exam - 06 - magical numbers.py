magic_number = int(input())

for a in range(1, magic_number + 1):
    for b in range(1, magic_number + 1):
        for c in range(1, magic_number + 1):
            for d in range(1, magic_number + 1):
                for e in range(1, magic_number + 1):
                    for f in range(1, magic_number + 1):

                        if (a * b * c * d * e * f) == magic_number:
                            print(f'{str(a)}{str(b)}{str(c)}{str(d)}{str(e)}{str(f)}')
