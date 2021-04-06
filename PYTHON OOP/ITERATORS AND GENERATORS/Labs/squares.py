def squares(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1


print(list(squares(5)))

# my_list = [1, 3, 6, 10]
# # print([x**2 for x in my_list])
#
# print((x**2 for x in my_list))
