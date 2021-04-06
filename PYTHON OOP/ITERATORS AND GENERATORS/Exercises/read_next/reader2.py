
def read_next(*args):
    for element in args:

        for e in element:
            yield str(e)


for item in read_next('string', (2, 3, 4, 5), {'d': 1, 'i': 2, 'c': 3, 't': 4}, [1, '2', 3, [4, 5, 6, '7']]):
    print(item, end='')


