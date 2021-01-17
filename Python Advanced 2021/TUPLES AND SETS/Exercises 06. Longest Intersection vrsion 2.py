n = int(input())
first_nums = set()
second_nums = set()

longest_set = set()

for _ in range(n):
    first, second = tuple(input().split('-'))

    first_start, first_end = tuple(map(int, first.split(',')))
    first_nums_set = set(range(first_start, first_end + 1))

    second_start, second_end = tuple(map(int, second.split(',')))
    second_nums_set = set(range(second_start, second_end + 1))

    intersect = first_nums_set & second_nums_set

    if len(intersect) > len(longest_set):
        longest_set = intersect

print(f"Longest intersection is {sorted(list(longest_set))} with length {len(longest_set)}")
