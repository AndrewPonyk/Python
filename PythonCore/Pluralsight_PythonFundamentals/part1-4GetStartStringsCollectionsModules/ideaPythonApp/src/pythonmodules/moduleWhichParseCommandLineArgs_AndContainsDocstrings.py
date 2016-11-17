""" Contains function to calculate power to 3 and can parse command line args

Usage:
    python3 moduleWhichParseCommandLineArgs_AndContainsDocstrings.py 12

"""

import math
import sys

__author__ = 'andrii'


def funcInModule(n):
    """ Returns number in pow 3
    Args :
        n: number to be powered

    Returns:
        A number in pow 3
    """
    print(math.pow(n, 3))
    return math.pow(n, 3);


if __name__ == "__main__" and len(sys.argv) > 1:
    funcInModule(int(sys.argv[1]));
