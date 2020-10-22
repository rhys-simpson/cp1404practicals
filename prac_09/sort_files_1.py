"""
CP1404 Practical - sort files
Rhys Simpson
"""

import shutil
import os


def main():
    """ """
    os.chdir('FilesToSort')
    print("Starting directory is: {}".format(os.getcwd()))

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split(".")[1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        shutil.move(filename, ("{}/" + filename).format(extension))


main()
