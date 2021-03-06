"""A module that converts a number from decimal to any base from 2 to 36"""

ENCODINGS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(numbers, number_map):
    '''For the numbers in given sequence, returns a string with numbers encoded'''
    if max(numbers) > len(number_map):
        raise ValueError("Cannot map some of the digits. Check number map")

    return ''.join(number_map[x] for x in numbers)


def convert_from_base10(number, base):
    """Gets a number and target base, returns the number in target base as string"""
    if not isinstance(number, int) or not isinstance(base, int):
        raise TypeError("Invalid type - number and base must be integer")

    if base <= 1:
        raise ValueError("Invalid valid - base must be >= 2")

    sign = -1 if number < 0 else 1
    number *= sign

    digits = []
    while number > 0:
        number, mod = divmod(number, base)
        digits.insert(0, mod)

    converted_number = encode(digits, ENCODINGS)

    if sign == -1:
        converted_number = "-" + converted_number

    return converted_number
