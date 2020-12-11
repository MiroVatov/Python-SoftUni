import re

n = int(input())
pattern = r'(U\$)(?P<user>[A-Z][a-z]{2,})\1(P@\$)(?P<pass>[A-Za-z]{5,}\d+)\3'
registrations = 0
for _ in range(n):
    username = input()
    if re.search(pattern, username):
        print(f'Registration was successful')
        registrations += 1
        for m in re.finditer(pattern, username):
            print(f"Username: {m.group('user')}, Password: {m.group('pass')}")
    else:
        print(f'Invalid username or password')

print(f'Successful registrations: {registrations}')
