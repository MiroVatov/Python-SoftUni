k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0
for symbol_1 in range(k, 9):
    if symbol_1 % 2 == 0:
        for symbol_2 in range(9, (l - 1), - 1):
            if symbol_2 % 2 != 0:
                for symbol_3 in range(m, 9):
                    if symbol_3 % 2 == 0:
                        for symbol_4 in range(9, (n - 1), - 1):
                            if symbol_4 % 2 != 0:
                                if counter == 6:
                                    break
                                if f'{symbol_1}{symbol_2}' == f'{symbol_3}{symbol_4}':
                                    print('Cannot change the same player.')
                                else:
                                    print(f'{symbol_1}{symbol_2} - {symbol_3}{symbol_4}')
                                    counter += 1