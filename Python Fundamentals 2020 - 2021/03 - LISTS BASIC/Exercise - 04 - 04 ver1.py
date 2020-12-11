nums_str = input().split(', ')
count = int(input())

nums = []

for ind in nums_str:
    nums.append(int(ind))

result_sum = [0] * count

for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]

print(result_sum)