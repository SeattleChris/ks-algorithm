#!/usr/bin/python3
import sys
import time


def decide_down(i, digits):
    """ INPUT: digits is full array of the digits of the num we are solving
        INPUT: i is an interator for the position in digits array we are evealuating.
        OUTPUT: Bool to indicate we should go down to find short path to all even digits
        If we go up we only need to get to _00, but going down will require moving
        past the change of number of digits down to _88 before they are all even.
        Therefore, we need to test against being above or below 44 for next 2 digits.
    """
    last_pos = len(digits) - 1
    if i + 2 > last_pos:  # We don't have 2 more digits after i'th position.
        if i + 1 > last_pos:  # We either are at last_pos or exceeded it somehow
            return True  # We have tested all digits and it could go up or down, assume down.
        # i is at second to last position, only evaluating last digit.
        return digits[i + 1] < 5  # Go down if we are at 10s and 1s is under 5; Up on 5 or higher.
    # we have at least two more digits after our current position.
    test = digits[i + 1] * 10 + digits[i + 2]
    if test == 44:
        return decide_down(i + 2, digits)
    return test < 44  # Go down if test < 44, go up if test > 44


def supervin_calc(t, *args):
    case_num = 0
    for num in args:
        case_num += 1
        digits = [int(char) for char in str(num)]
        num = int(num)
        go_down, count, i = False, 0, 0
        # skip all leading even digits
        while i < len(digits) and not digits[i] % 2:
            i += 1
        if i == len(digits):  # no odd digits found
            print(f'Case #{case_num}: 0')
            continue  # skip to next num in args
        elif i == len(digits) - 1:  # the only odd digit is in ones place
            print(f'Case #{case_num}: 1')
            continue  # skip to next num in args
        # i is now at the first odd digit in our given num and it's not the ones place
        # if first odd digit is 9, going down is quickest, otherwise it depends on following digits
        go_down = True if digits[i] == 9 else decide_down(i, digits)
        i += 1
        # up, !down | !up, down | up, down | !up !down
        # count how many clicks to make it 1 away from our goal.
        for k in range(i, len(digits)):
            dig_move = digits[k] + 1 if go_down else 10 - digits[k] - 1
            count += dig_move * 10 ** (len(digits) - i - 1)
        # one click away from our goal
        count += 1
        print(f'Case #{case_num}: {count}')
    # end supervin_calc


if __name__ == '__main__':
    args = []
    filename, t, *args = sys.argv
    start = time.time()
    supervin_calc(t, *args)
    durr = time.time() - start
    if durr > int(t) * 20 * 1000:
        print('Fail: ', durr)
    else:
        print('Succcess!', durr)
