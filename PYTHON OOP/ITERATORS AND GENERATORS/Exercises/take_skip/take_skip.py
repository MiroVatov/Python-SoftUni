class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.count:
            num = self.number
            self.number += self.step
            self.counter += 1
            return num
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
