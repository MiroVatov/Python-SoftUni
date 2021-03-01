numbers = list(map(int, input().split()))

negatives = filter(lambda number: number < 0, numbers)
positives = filter(lambda number: number > 0, numbers)

# We can iterate only once per MAP function, second iteration will throw zero value

sum_negatives = sum(negatives)
sum_positives = sum(positives)

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print(f"The negatives are stronger than the positives")
elif abs(sum_negatives) < sum_positives:
    print("The positives are stronger than the negatives")