num = int(input())
lst = []

def loading_bar(num):

    for n in range(0, 100 + 1, 10):
        if n % 10 == 0 and n <= num and n > 0:

            lst.append('%')

        elif n % 10 == 0 and n > num and n > 0:

            lst.append('.')

    return num


if loading_bar(num) < 100:
    for i in lst:
        lst = ''.join(lst)
    print(f'{num}% [{lst}]')
    print(f'Still loading...')
else:
    for i in lst:
        lst = ''.join(lst)
    print(f'{num}% Complete!')
    print(f'[{lst}]')