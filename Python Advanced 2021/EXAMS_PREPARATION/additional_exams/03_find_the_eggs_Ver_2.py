def find_sub_matrix(n_l, n):
    subs_matrix = []
    for i in range(n):
        subs_matrix.append(n_l[i:len(n_l):n])
    return subs_matrix


def find_strongest(r):
    max_num = max(r)
    if not max_num == r[0] and not max_num == r[-1]:
        return max_num
    return


def find_strongest_eggs(*args):
    result = []
    nums_list, n = args
    if n > 1:
        sub_matrix = find_sub_matrix(nums_list, n)
        for row in sub_matrix:
            stronger_egg = find_strongest(row)
            if stronger_egg:
                result.append(stronger_egg)
    else:
        result = [find_strongest(nums_list)]
    return result


test = ([-1, 7, 3, 15, 2, 12, 5, 90, 18, 1, 89, 33], 3)
print(find_strongest_eggs(*test))

# test = ([-1, 7, 3, 15, 2, 12, 6, 7, 8], 3)
# print(find_strongest_eggs(*test))
# test = ([-1, 0, 2, 5, 2, 3], 2)
# print(find_strongest_eggs(*test))
# test = ([51, 21, 83, 52, 55], 1)
# print(find_strongest_eggs(*test))