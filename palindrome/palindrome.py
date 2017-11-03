from baseconvert.baseconvert import base


def palindrome(string):
    """
    Given a string, returns true or false if it's a palindrome or not.

    Args
    ----
    string: string
        string to be evaluated as palindrome

    Returns
    -------
    boolean
        Returns True if palindrome or False otherwise
    """
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and palindrome(string[1:-1])


def min_base(digit):
    """
    Given a integer, returns the minimum base in which the digit is a palindrome.

    Args
    ----
    digit: integer
        number to be evaluated as palindrome

    Returns
    -------
    base_number: integer
        Returns the minimum base number
    """
    base_number = 1
    is_palindrome = True

    while is_palindrome:
        base_number += 1
        is_palindrome = not (palindrome(base(digit, 10, base_number, string=True)))

    return base_number
