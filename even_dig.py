#!/usr/bin/python3
import sys


def digit_to_even(digit, delta, move_up, move_down):
    if move_up:
        return 10 - digit
    elif move_down:
        return digit
    return 1 if digit % 2 else 0

    # end def digit_to_even


def decide_up_down(i, digits):
    """ INPUT: digits is full array of the digits of the num we are solving
        INPUT: i is an interator for the position in digits array we are evealuating.
        This function is ONLY called if digits[i] is odd.
        OUTPUT: 2-tuple of bool if going up or down will get us to even.
        If we go up we only need to get to _00, but going down will require moving
        past the change of number of digits down to _88 before they are all even.
        Therefore, we need to test against being above or below 44 for next 2 digits.
    """
    if not digits[i] % 2:
        raise ValueError('Called decide_up_down on an even digit')
    if len(digits) - 1 < i + 2:  # We don't have 2 more digits
        if len(digits) - 1 < i + 1:  # We don't have 1 more digit
            return (False, False)
            # return (True, True) if digits[i] % 2 else (False, False)
        go_up = True if digits[i + 1] > 4 else False
        go_down = True if digits[i + 1] < 6 else False
        return (go_up, go_down)
    # we have at least two more digits after our current position.
    test = digits[i + 1] * 10 + digits[i + 2]
    if test == 44:
        i += 2
        while not digits[i] % 2:
            i += 1
            # Return either direction works if we've exhausted all digits
            if i == len(digits):
                return (True, True)
        # i is now at next odd digit
        return decide_up_down(i, digits)
    go_up = True if test > 44 else False
    go_down = True if test < 44 else False
    return (go_up, go_down)


def supervin_calc(t, *args):

    case_num = 0
    for num in args:
        case_num += 1
        digits = [int(char) for char in str(num)]
        num = int(num)
        go_up, go_down, count, i = False, False, 0, 0
        # skip all leading even digits
        while i < len(digits) and not digits[i] % 2:
            i += 1
        # Return 0 moves needed if we've exhausted all digits
        if i == len(digits):
            print(f'Case #{case_num}: 0')
            continue  # skip to next num in args
        # i is now at the first odd digit in our given num
        # if first odd digit is 9, going down is quickest
        # otherwise we go up or down depending on the following digits
        flag = True if digits[i] == 1 else False
        if digits[i] == 9:
            go_up, go_down = False, True
        else:
            (go_up, go_down) = decide_up_down(i, digits)
        # (go_up, go_down) = decide_up_down(i, digits) if digits[i] != 9 else False, True

        # _100, _10
        for k in range(len(digits) - 1, i - 1, -1):

            count += digit_to_even(digits[k], flag, go_up, go_down) * 10 ** k
        print(f'Case #{case_num}: {count}')


        # for i in range(1, len(digits)):
            # move = 0
            # if digits[i] == 9:
            #     pass
            # else:
            #     move = digit_to_even(digits[i], go_up, go_down) * 10 ** (len(digits) - i - 1)



            # if go_up:
            #     count += (10 - digits[i]) * 10 ** (len(digits) - i - 1)
            # if go_down:
            #     pass
            # if digits[i] % 2:  # this digit is odd
            #     if digits[i+1] > 4:
            #         go_up = True
            #     else:
            #         go_down = True
# 1011 - 3 = 998
    # end def supervin_calc
# 1599: at digits[1] & go_up == True --> 5 * 100
# 1499:
# 749 --> 688 or 800
# 756 --> 688 or 800
# if first digit is odd, but not 9, if next digit is > 4 then going up is quickest (for positive integers)
# if leading digits are even, we can ignore them. AKA 2299 ~= 99, 4831 ~= 31
# 309 --> 288 or 400? --> move down 21 or up


if __name__ == '__main__':
    args = []
    filename, t, *args = sys.argv
    # start = time.time()
    supervin_calc(t, *args)
