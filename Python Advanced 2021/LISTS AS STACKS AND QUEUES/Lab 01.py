initial_text = input()
stack = []

for ch in initial_text:
    stack.append(ch)

reversed_text = []
while len(stack) > 0:
    pop_char = stack.pop()
    reversed_text.append(pop_char)

print(''.join(reversed_text))