"""
CP1404 - Practical
Store users emails

Rhys Simpson
"""


def main():
    """Create dictionary of emails and names"""
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        choice = input("Is your name {}? (Y/n) ".format(name))
        if choice.upper() != "Y" and choice != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    """Get the name from the email address"""
    split_name = email.split("@")[0]
    parts = split_name.split(".")
    name = " ".join(parts).title()
    return name


main()
