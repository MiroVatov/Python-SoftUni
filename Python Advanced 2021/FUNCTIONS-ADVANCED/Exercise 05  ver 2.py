command = input()
nums = list(map(int, input().split()))

if command == 'Odd':
    odd_sum = filter(lambda n: n % 2 != 0, nums)
    print(sum(odd_sum) * len(nums))
elif command == 'Even':
    even_sum = filter(lambda n: n % 2 == 0, nums)
    print(sum(even_sum) * len(nums))