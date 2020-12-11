num = int(input())


def deviders(num):
    devider = []
    for i in range(1, num + 1):
        if num % i == 0 and i < num:
            devider.append(i)
    return sum(devider)
if deviders(num) == num and num > 0:
    print(f'We have a perfect number!')
else:
    print(f'It\'s not so perfect.')
