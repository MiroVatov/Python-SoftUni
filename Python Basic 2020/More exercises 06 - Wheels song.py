control_number = int(input())
count_result = 0

count = False
for a in range(1, 10):
    for b in range(1, 10):

        for c in range(1, 10):
            for d in range(1, 10):

                result = (a * b) + (c * d)

                if result == control_number and a < b and c > d:

                        count_result += 1
                        print(f'{a}{b}{c}{d}', end=' ')
                else:
                    continue
                if count_result == 4:
                    count = True
                    password = (f'{a}{b}{c}{d}')

                else:
                    continue
print()
if count == True:
    print(f'Password: {password}')
else:
    print('No!')
