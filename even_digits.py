#!/usr/bin/python3
import sys
import time


def even_digits_small_data(t, *args):
    """ The small data set has maximum values of 10 ** 5
        For these a brute force approach is sufficiently quick.
    """

    def test_digits(num):
        for ea in [int(char) for char in str(num)]:
            if ea % 2:
                return False
        return True

    case_num = 0
    for num in args:
        case_num += 1
        num = int(num)
        is_even, i = False, -1
        while is_even is False:
            i += 1
            is_even = test_digits(num + i) or test_digits(num - i)
        print(f'Case #{case_num}: {i}')
    # end even_digits_small_data


def even_digits_large_data(t, *args):
    """ The large data set has has values greater than 10 ** 5
        For these, it is worth doing a computation to more quickly
        discover our answer.
    """

    def decide_down(i, digits):
        last_pos = len(digits) - 1
        if i + 2 > last_pos:
            if i + 1 > last_pos:
                return True
            return digits[i + 1] < 5
        test = digits[i + 1] * 10 + digits[i + 2]
        if test == 44:
            return decide_down(i + 2, digits)
        return test < 44

    case_num = 0
    for num in args:
        case_num += 1
        num = int(num)
        digits = [int(char) for char in str(num)]
        go_down, count, i = False, 0, 0
        # skip all leading even digits
        while i < len(digits) and not digits[i] % 2:
            i += 1
        if i == len(digits):  # no odd digits found
            print(f'Case #{case_num}: 0')
            continue
        elif i == len(digits) - 1:
            print(f'Case #{case_num}: 1')
            continue
        # i is now at the first odd digit in our given num and it's not the ones place
        go_down = True if digits[i] == 9 else decide_down(i, digits)
        # count how many clicks to make it 1 away from our goal.
        for k in range(i + 1, len(digits)):
            dig_move = digits[k] + 1 if go_down else 10 - digits[k] - 1
            count += dig_move * 10 ** (len(digits) - k - 1)
        count += 1
        print(f'Case #{case_num}: {count}')
    # end even_digits_large_data


if __name__ == '__main__':
    args = []
    filename, t, *args = sys.argv
    # TODO: setup paramter or flag to run small data version of code.
    start = time.time()
    even_digits_large_data(t, *args)
    durr = time.time() - start
    if durr > int(t) * 20 * 1000:
        print('Fail: ', durr)
    else:
        print('Succcess!', durr)
