from collections import deque


def list_manipulator(numbers: list, *args):
    action, position = args[0], args[1]
    unpacked = list(args[2:])

    if action == 'add':
        if position == 'beginning':
            numbers = [i for i in unpacked] + numbers
            return numbers

        elif position == 'end':
            numbers = numbers + [i for i in unpacked]
            return numbers

    elif action == 'remove':
        if position == 'beginning':
            numbers = deque(numbers)
            if unpacked:
                [numbers.popleft() for _ in range(*unpacked)]
                return list(numbers)

            else:
                numbers.popleft()
                return list(numbers)

        elif position == 'end':
            if unpacked:
                [numbers.pop() for _ in range(*unpacked)]
                return numbers
            else:
                numbers.pop()
                return numbers


print(list_manipulator([1,2,3,4,5,6], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3,4], "add", "end", 30))
print(list_manipulator([1,2,3,8,9], "remove", "end", 2))
print(list_manipulator([99,8,1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))



