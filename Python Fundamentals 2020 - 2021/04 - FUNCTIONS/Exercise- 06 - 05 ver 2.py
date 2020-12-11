def palindrome_checker(num_str):
    return True if num_str == num_str[::-1] else False

num_str_list = input().split(', ')

for num_str in num_str_list:
    print(palindrome_checker(num_str))