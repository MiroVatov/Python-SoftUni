from collections import deque


class sequence_repeat:
    def __init__(self, seq: str, number: int):
        self.seq = list(seq)
        self.number = number
        self.numbers_deque = deque(self.seq)

    def __iter__(self):
        return self

    def __next__(self):

        # Variant 1 -->>

        # while self.number > 0:
        #     element = self.numbers_deque.popleft()
        #     self.number -= 1
        #     self.numbers_deque.append(element)
        #     return element
        #
        # raise StopIteration()

        # Variant 2 -->>

        if self.number == 0:
            raise StopIteration

        element = self.numbers_deque.popleft()
        self.number -= 1
        self.numbers_deque.append(element)
        return element


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
