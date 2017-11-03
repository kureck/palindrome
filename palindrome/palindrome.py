from baseconvert.baseconvert import base


def palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and palindrome(string[1:-1])


def min_base(digit):
    base_number = 1
    is_palindrome = True

    while is_palindrome:
        base_number += 1
        is_palindrome = not (palindrome(base(digit, 10, base_number, string=True)))

    return base_number
