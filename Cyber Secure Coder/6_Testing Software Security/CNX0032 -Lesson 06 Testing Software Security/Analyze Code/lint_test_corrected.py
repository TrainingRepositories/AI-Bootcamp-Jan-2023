"""
Test Script for use with Static Code Analysis
specifically pylint
"""


def long_division(numerator, denominator):
    """
    Divide numerator by the demoninator and return the resulting floating pointe number
    """
    if denominator != 0:
        value = float(numerator) / float(denominator)
    else:
        value = 0.0
    return value


def main():
    """
    main entry, no arguments or return values
    """
    print(long_division(27, 0))


if __name__ == '__main__':
    main()
