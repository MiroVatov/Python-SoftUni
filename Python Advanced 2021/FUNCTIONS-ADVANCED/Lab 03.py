def multiply(*args):
    res = 1
    for a in args:
        res *= a
    return res


nums = input().split(', ')
print(multiply(4, 5, 6, 1, 3))


# from functools import reduce
#
#
# def multiply(*args):
#     return reduce(lambda a, b: a * b, args)
#
#
# print(multiply(4, 5, 6, 1, 3))