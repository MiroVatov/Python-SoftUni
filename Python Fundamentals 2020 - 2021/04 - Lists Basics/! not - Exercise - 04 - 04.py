beggars_catch = input()
beggars_catch = beggars_catch.split(', ')
lst_beggars = list(beggars_catch)
number_of_beggars = int(input())

new_list1 = []
new_list2 = []
first = 0
second = 0
for i in range(number_of_beggars):

    for b in lst_beggars:
        if int(b) % 2 == 0:
            second += int(b)

        elif int(b) % 2 != 0:
            first += int(b)
first = int(first / number_of_beggars)
second = int(second / number_of_beggars)
new_list1.append(first)
new_list1.append(second)

print(new_list1)
#print(new_list2)

