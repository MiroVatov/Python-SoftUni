
def read_next(*args):
    element = args

    for el in element:

        if isinstance(el, dict):
            for e in el.keys():
                yield str(e)

        elif isinstance(el, tuple):
            for e in el:
                yield str(e)

        elif isinstance(el, str):
            yield str(el)

        elif isinstance(el, list):
            for e in el:
                yield str(e)


for item in read_next('string', (2, 3, 4, 5), {'d': 1, 'i': 2, 'c': 3, 't': 4}, [1, '2', 3, [4, 5, 6, '7']]):
    print(item, end='')


