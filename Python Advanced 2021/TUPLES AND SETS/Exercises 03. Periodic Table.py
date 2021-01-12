num = int(input())

unique_elements = set()

for _ in range(num):
    element = input().split()
    if len(element) > 1:
        for el in element:
            unique_elements.add(el)
    else:
        unique_elements.add(''.join(element))

print('\n'.join(unique_elements))