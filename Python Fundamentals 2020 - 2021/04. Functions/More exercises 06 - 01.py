res = 0

def text_checker(res):
    text_int_float = input()
    if text_int_float == 'int':
        digit = int(input())
        res = digit * 2
        print(res)

    elif text_int_float == 'real':
        digit = float(input())
        res = digit * 1.5
        print(f'{res:.2f}')

    else:
        string = input()
        res = string
        print(f'${res}$')

text_checker(res)