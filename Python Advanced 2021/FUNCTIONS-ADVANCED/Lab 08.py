from itertools import permutations
from itertools import chain

numbers = [n for n in input().split(', ')]
n = len(numbers)

permutate = set(permutations(['-'] * n + ['+'] * n, n))

for per in permutate:
    mutant = ''.join(chain(*zip(per, numbers)))
    res = eval(mutant)
    print(f'{mutant}={res}')
