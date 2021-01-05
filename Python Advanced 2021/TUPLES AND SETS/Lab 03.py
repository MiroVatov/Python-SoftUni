n_names = int(input())

names = set()

for n in range(n_names):
    names.add(input())

# for person in names:
#     print(person)

print('\n'.join(names))