first_str = input()
second_str = input()

while first_str in second_str:
    second_str = second_str.replace(first_str,'')

print(second_str)

# first_string = [t.split() for t in input()]
# second_string = [w.split() for w in input()]
#
# third_list = [x for x in second_string if x not in first_string]
#
# outlist = [''.join([c for c in lst]) for lst in third_list]
# final_str = ''.join(outlist)

# print(final_str)

""""

first_str = input()
second_str = input()

third_str = [x for x in second_str if x not in first_str]

print(''.join(third_str))

"""