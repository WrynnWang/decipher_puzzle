import sys
from base32_to_int import *
from int_to_five_digits_binary import *
from binary_to_two_digits_hex import *

def main():
    base32_to_int()
    int_to_five_digits_binary()
    binary_to_two_digits_hex()


if __name__ == '__main__':
    sys.exit(main())