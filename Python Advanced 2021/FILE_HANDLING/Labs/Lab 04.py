import os

try:
    os.remove('exercise01.txt')
    print('Successfully deleted')
except FileNotFoundError:
    print('File already deleted!')
