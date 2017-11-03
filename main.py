from palindrome.palindrome import min_base


if __name__ == '__main__':
    N = range(1, 1001)
    for n in N:
        print("{}, {}".format(n, min_base(n)))
