#!/usr/bin/python3
import sys


def guess_num(low, high, chances):
    """ All inputs are integers:
        low is inclusive lower bound
        high is exclusive upper bound
        chances is number of guesses we get
        Output is Bool for solving it in time.
    """
    for count in range(0, chances):
        # compute guess
        q = low + (high - low) / 2
        # ask guess
        print(q)
        response = sys.stdin.read()
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


t = sys.stdin.read()
for count in range(0, t):
    a, b = sys.stdin.read().split()
    n = sys.stdin.read()
    solved = guess_num(int(a), int(b), int(n))
    if solved is False:
        break
