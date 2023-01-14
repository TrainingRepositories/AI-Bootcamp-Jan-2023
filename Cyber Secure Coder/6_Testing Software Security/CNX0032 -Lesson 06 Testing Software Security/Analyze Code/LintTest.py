"""
Test Script for use with Static Code Analysis
specifically pylint
"""


def divide_numbers(a, b):
    c = float(a) / float(b)
    return c


def main():
    # main entry, no arguments or return values
    print(divide_numbers(27, 0))


if __name__ == '__main__':
    main()
