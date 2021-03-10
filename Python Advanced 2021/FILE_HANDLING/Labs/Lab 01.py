import os.path

try:
    # open('/media/miroslav/New Disc/Miro/programs/SoftUni/Python Advanced - May 2020/Project Advanced May - Sep 2020/COMPREHENSION/Exercise 02.py')
    with open('my_first_file.txt', 'r') as file:
        print('File exists')

except FileNotFoundError:
    print('File not found')

# print('File exists' if os.path.exists('exercise01.txt') else 'File not found')
