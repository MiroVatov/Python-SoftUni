n = int(input())
special_word = input()
special_list = []
lst = []

for i in range(n):
    word = input()
    lst.append(word)
    if special_word in word:
        special_list.append(word)
print(lst)
print(special_list)
