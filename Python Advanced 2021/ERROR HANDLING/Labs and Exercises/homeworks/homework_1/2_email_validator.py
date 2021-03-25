from Error_handling.Exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError
from Error_handling.helpers import VALID_DOMAINS

command = input()

def valid_email(email):
    if "@" in email:
        name, domain = email.split('@')
    else:
        raise MustContainAtSymbolError("Email must contain ")
    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")

    try:
        website, extension = domain.split('.')
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if not extension in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    return True


while command != "End":
    if valid_email(command):
        print("Email is valid")
    command = input()


