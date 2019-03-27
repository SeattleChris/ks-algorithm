#!/usr/bin/python3


def guess_num(low, high, chances):
    """ All inputs are integers:
        low is inclusive lower bound
        high is exclusive upper bound
        chances is number of guesses we get
        Output is Bool for solving it in time.
    """
    for count in range(0, chances):
        # compute guess
        q = low + (high - low) // 2
        # ask guess
        print(q)
        response = input()
        # parse answer
        if response == 'TOO_SMALL':
            low = q + 1
        elif response == 'TOO_BIG':
            high = q
        elif response == 'CORRECT':
            return True
        elif response == 'WRONG_ANSWER':
            return False
    return False


t = input()
for count in range(0, int(t)):
    a, b = input().split()
    n = input()
    solved = guess_num(int(a), int(b), int(n))
    if solved is False:
        break

# end of number_guess.py
