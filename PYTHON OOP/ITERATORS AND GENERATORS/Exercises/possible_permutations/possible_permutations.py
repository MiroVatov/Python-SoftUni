from itertools import permutations
from collections import deque


def possible_permutations(data):

    # Variant 1 -->>

    # permutated_data = deque(permutations(data))
    # while permutated_data:
    #     data = permutated_data.popleft()
    #     yield list(data)

    # Variant 2 -->>

    for el in permutations(data):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]

# [print(n) for n in possible_permutations([1, 2, 3, 4, 5])]