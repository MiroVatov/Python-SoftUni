initial_array = input().split()
initial_array = [int(x) for x in initial_array]

avg_array = sum(initial_array) / len(initial_array)

top_five = [a for a in initial_array if a > avg_array]


final_list = []
sorted_top_five = sorted(top_five, reverse=True)

for i in sorted_top_five:
    final_list.append(i)
    if len(final_list) == 5:
        break

if len(final_list) == 0:
    print("No")
else:
    print(' '.join(map(str, final_list)))

