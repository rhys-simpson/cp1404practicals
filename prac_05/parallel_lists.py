"""
CP1404 Practical
Convert parallel lists
Rhys Simpson
"""


def main():
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    example = convert_lists_to_dict(names, dates_of_birth)
    print(example)


def convert_lists_to_dict(names, dates_of_birth):
    dictionary = {}
    for name in names:
        for date in dates_of_birth:
            dictionary[name] = date
    return dictionary


main()
