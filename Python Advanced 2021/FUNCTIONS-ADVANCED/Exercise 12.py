# Variant 1 ------>
#
# def is_palindrome(word):
#     middle = len(word) // 2
#     first_half = word[:middle]
#     second_half = word[middle + 1:]
#     for first, second in zip(first_half, reversed(second_half)):
#         if first != second:
#             return False
#     return True
#
#
# print(is_palindrome("abdefcfedba"))
# print(is_palindrome("peter"))


# Variant 2 ------>
#

def palindrome(word, index):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"

#
# print(is_palindrome("abdefcfedba"))
# print(is_palindrome("peter"))


# VARIANT 3 with recursion --->

# def palindrome(word):
#     if len(word) == 0:
#         return True
#     if len(word) == 1:
#         return True
#     if word[0] == word[-1]:
#         return palindrome(word[1:-1])
#
#     # return False


print(palindrome("abba", 0))
print(palindrome("peter", 0))


# def palindrome(word, idx):
#     if idx == len(word) // 2:  # ''
#         return f"{word} is a palindrome"
#     if word[idx] != word[len(word) - 1 - idx]:  # 'c'
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, idx + 1)
#
#
# print(palindrome("abdefcfedba", 0))
# print(palindrome("peter", 0))