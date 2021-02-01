phones_dict = {}
command = input()

while not command.isdigit():
    name, phone = command.split('-')
    phones_dict[name] = phone
    command = input()

nums = int(command)
for _ in range(nums):
    person = input()
    if person in phones_dict:
        result = ''.join(person + ' -> ' + phones_dict[person])
        print(result)
    else:
        print(f"Contact {person} does not exist.")