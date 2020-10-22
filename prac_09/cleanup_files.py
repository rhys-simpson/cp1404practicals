"""
CP1404 Practical
Cleanup files program
"""
import shutil
import os


def main():
    """os module functions."""
    os.chdir('Lyrics')
    print("Starting directory is: {}".format(os.getcwd()))

    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            # file_name = os.path.join(directory_name, filename)
            # new_name = os.path.join(directory_name, get_fixed_filename(filename))
            # os.rename(file_name, new_name)

    # options -
    # Option 1: rename file to new name - in place
    # os.rename(filename, new_name)

    # Option 2: move file to new place, with new name
    # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # Example: Away In A Manger.txt -> Away_In_A_Manger.txt
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
