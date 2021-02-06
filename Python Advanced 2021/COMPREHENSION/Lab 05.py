nums = list(range(2, 11))
start = int(input())
end = int(input())
filtered = [num for num in range(start, end + 1) if any([num % x == 0 for x in nums])]
print(filtered)