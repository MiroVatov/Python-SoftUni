import itertools

initial_text = input()

new_text = ''.join(g[0] for g in itertools.groupby(initial_text))

print(new_text)

# def remove_repeated_characters(s):
#     groups = itertools.groupby(s)
#     cleaned = ''.join(g[0] for g in groups)
#     return cleaned

# print(remove_repeated_characters(initial_text))
