"""
CP1404 Practical - wikipedia API
Rhys Simpson
"""

import wikipedia


def main():
    """ """
    try:
        user_search = input("What do you want to search for? ")
        page = wikipedia.page(user_search)
        print("{} \n{} \n{}".format(page.title, page.summary, page.url))
        while user_search != "":
            user_search = input("What do you want to search for? ")
            page = wikipedia.page(user_search)
            print("{} \n{} \n{}".format(page.title, page.summary, page.url))
    except wikipedia.exceptions.WikipediaException:
        quit()


main()
