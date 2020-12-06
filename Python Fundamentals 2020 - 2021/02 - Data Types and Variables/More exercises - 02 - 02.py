a = int(input())
b = int(input())


print('Before:')
print(f'a = {a}')
print(f'b = {b}')

b1 = a
a = b
b = b1

print('After:')
print(f'a = {a}')
print(f'b = {b}')
