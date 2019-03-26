#!/usr/bin/python3
import sys
# import time


def test_digits(num):
    for ea in [int(char) for char in str(num)]:
        if ea % 2:
            return False
    return True


def supervin_calc(t, *args):
    if int(t) != len(args):
        print('Data malformed', t, len(args))
    j = 0
    for num in args:
        num = int(num)
        j += 1
        is_even, i = False, -1
        while is_even is False:
            i += 1
            is_even = test_digits(num + i) or test_digits(num - i)
        print('Case #', j, ': ', i)


if __name__ == '__main__':
    args = []
    filename, t, *args = sys.argv
    # start = time.time()
    supervin_calc(t, *args)
    # durr = time.time() - start
    # if durr > int(t) * 20 * 1000:
    #     print('Fail: ', durr)
    # else:
    #     print('Succcess!', durr)
