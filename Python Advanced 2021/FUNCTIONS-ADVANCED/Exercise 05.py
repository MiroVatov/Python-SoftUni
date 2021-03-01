command = input()
nums = list(map(int, input().split()))

if command == 'Odd':
    print(sum([n for n in nums if n % 2 != 0]) * len(nums))
elif command == 'Even':
    print(sum([n for n in nums if n % 2 == 0]) * len(nums))