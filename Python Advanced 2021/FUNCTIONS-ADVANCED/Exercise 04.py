nums = list(map(int, input().split()))
sum_positives = sum([n for n in nums if n >= 0])
sum_negatives = sum([n for n in nums if n < 0])

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')