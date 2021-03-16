class NameTooShortError(Exception):
    """
    raise it when the name in the email is less than or equal to 4
    """
    def __init__(self, msg="Name must be more than 4 characters"):
        self.msg = msg
        super().__init__(msg)


class MustContainAtSymbolError(Exception):
    """
    raise it when there is no "@" in the email
    """

    def __init__(self, msg="Email must contain @"):
        self.msg = msg
        super().__init__(msg)


class InvalidDomainError(Exception):
    """
     "Domain must be one of the following: .com, .bg, .org, .net"
    """

    def __init__(self, msg="Domain must be one of the following: .com, .bg, .org, .net"):
        self.msg = msg
        super().__init__(msg)


# def is_valid_email(email, em_name, sep, dom):
#     if len(em_name) > 4 and sep in email and dom in valid_domains:
#         return True
#     return False


def valid_username(name):
    if len(name) <= 4:
        raise NameTooShortError()


def validate_at_symbol(email):
    if '@' not in email:
        raise MustContainAtSymbolError()


def validate_domain(dom, valid_domains):
    if dom not in valid_domains:
        raise InvalidDomainError()


separator = "@"
valid_domains = ['com', 'bg', 'org', 'net']

while True:

    email = input()
    if email == 'End':
        break

    username = email.split('@')[0]
    domain = email.split('.')[-1]

    valid_username(username)
    validate_at_symbol(email)
    validate_domain(domain, valid_domains)

    print("Email is valid")



