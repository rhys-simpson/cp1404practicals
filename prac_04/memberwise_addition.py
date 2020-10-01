"""
CP1404 practical
memberwise addition
"""
# TODO make so lists can be different sizes


def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    answer = add_memberwise(a, b)
    print(answer)


def add_memberwise(a, b):
    longest_list = 0
    if len(list(b)) > len(list(a)):
        longest_list += len(list(b))
    else:
        longest_list += len(list(a))

    result_list = []
    for i in range(0,  longest_list):
        result_list.append(a[i] + b[i])
    return result_list


main()
