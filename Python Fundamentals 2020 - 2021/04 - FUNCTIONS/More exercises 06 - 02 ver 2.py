res = 0

def text_checker(res):
    text_int_float = input()

    if text_int_float == 'int':
        digit = int(input())
        res = digit * 2
        return res

    elif text_int_float == 'real':
        digit = float(input())
        res = digit * 1.5
        return f'{res:.2f}'

    else:
        string = input()
        res = string
        return f'${res}$'

print(text_checker(res))