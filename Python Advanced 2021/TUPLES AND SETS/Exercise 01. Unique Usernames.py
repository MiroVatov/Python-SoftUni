n_names = int(input())

unique_names = set()

for _ in range(n_names):
    unique_names.add(input())

print(f'\n'.join(unique_names))

