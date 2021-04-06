from collections import deque


class vowels:

    vowels_list = ['A', 'a', 'O', 'o', 'E', 'e', 'U', 'u', 'I', 'i', 'Y', 'y']

    def __init__(self, some_text):
        self.some_text = deque(some_text)

    def __iter__(self):
        return self

    def __next__(self):

        while self.some_text:
            letter = self.some_text.popleft()
            if letter in vowels.vowels_list:
                return letter
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


def vowels(text):
    vowels_list = ['A', 'a', 'O', 'o', 'E', 'e', 'U', 'u', 'I', 'i', 'Y', 'y']
    return (ch for ch in text if ch in vowels_list)


print()
text = vowels('Abcedifuty0o')
for c in text:
    print(c)
