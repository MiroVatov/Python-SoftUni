from sys import maxsize

max_len = -maxsize

n = int(input())
longest_intersection = []
first_nums = set()
second_nums = set()
intersection = []

for _ in range(n):
    range_data = input().split('-')
    first = range_data[0].split(',')
    second = range_data[1].split(',')
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])
    first_nums = set(range(first_start, first_end + 1))
    second_nums = set(range(second_start, second_end + 1))
    inter = first_nums.intersection(second_nums)
    intersection.append(inter)
len_longest_intersection = max(len(s) for s in intersection)

for intersect in intersection:
    if len(intersect) > max_len:
        max_len = len(intersect)
        longest_intersection = intersect
print(f"Longest intersection is {list(longest_intersection)} with length {len_longest_intersection}")
