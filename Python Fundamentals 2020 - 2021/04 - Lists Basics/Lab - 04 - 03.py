n = int(input())
positive_list = []
negative_list = []
pos = 0
neg = 0
for i in range(n):
    num = int(input())
    if num > 0:
        positive_list.append(num)
        pos += 1
    elif num < 0:
        negative_list.append(num)
        neg += num

print(positive_list)
print(negative_list)
print(f'Count of positives: {pos}. Sum of negatives: {neg}')