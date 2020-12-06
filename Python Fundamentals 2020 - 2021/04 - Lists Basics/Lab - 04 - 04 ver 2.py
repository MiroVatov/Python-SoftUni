n = int(input())
special_word = input()
lst = []
special_string = []

for i in range(n):
    word = input()
    lst.append(word)
print(lst)

for i in range(len(lst)):
    element = lst[i]
    if special_word in element:
        special_string.append(element)

print(special_string)