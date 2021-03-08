def even_odd(*args):
    result = []
    cmd = args[-1]
    if cmd == 'even':
        result = [i for i in args[:-1] if i % 2 == 0]

    elif cmd == 'odd':
        result = [i for i in args[:-1] if i % 2 != 0]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
