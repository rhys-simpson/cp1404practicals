"""
CP1404 - Practical
Check password

Rhys Simpson
"""

MINIMUM_LENGTH = 3


def main():

    # Use functions to get and print password
    password = get_password()
    print_asterisks(password)


def get_password():
    # Get password from user
    password = input("Enter a password at least {} characters long: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password")
        password = input("Enter a password at least {} characters long: ".format(MINIMUM_LENGTH))
    return password


def print_asterisks(password):
    # Print password using '*' by number of characters in password
    print("*" * len(password))


main()
