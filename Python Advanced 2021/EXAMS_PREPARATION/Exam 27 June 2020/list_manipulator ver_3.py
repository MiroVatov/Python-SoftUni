

def list_manipulator(nums, action, position, *args):
    nums, action, position, *unpacked = (nums, action, position, *args)
    if action == 'add':
        if position == 'beginning':
            nums = [i for i in unpacked] + nums
            return nums

        elif position == 'end':
            nums = nums + [i for i in unpacked]
            return nums

    elif action == 'remove' and position == 'beginning':
        if args:
            del nums[:unpacked[0]]
            return nums

        del nums[0]
        return nums

    elif action == 'remove' and position == 'end':
        if args:
            del nums[-unpacked[0]:]
            return nums
        del nums[-1:]
        return nums


print(list_manipulator([1,2,3,4,5,6], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3,4], "add", "end", 30))
print(list_manipulator([1,2,3,8,9], "remove", "end", 2))
print(list_manipulator([99,8,1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))