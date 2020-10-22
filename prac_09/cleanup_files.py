"""
CP1404 Practical
Cleanup files program
"""

import os


def main():
    """os module functions."""
    os.chdir('Lyrics')
    print("Starting directory is: {}".format(os.getcwd()))

    for directory_name, sub_directories, filenames in os.walk('.'):
        for filename in filenames:
            file_name = os.path.join(directory_name, filename)
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(file_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    file_name = filename.replace(".TXT", ".txt").replace(" ", "_")
    previous_string = ""
    string = ""
    for char in file_name:
        if char.isupper() and previous_string.isalpha():
            string += "_"
        if not previous_string.isalpha() and previous_string != "'":
            char = char.upper()
        string += char
        previous_string = char
    return string.replace(".Txt", ".txt")


main()
