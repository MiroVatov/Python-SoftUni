elements = input().split(" ")

elements_dict = {}

for e in range(0, len(elements), 2):
    el_key = elements[e]
    el_value = elements[e + 1]
    elements_dict[el_key] = int(el_value)

print(elements_dict)