# Given three integers, this function returns true if the numbers are a Pythagorean Triple


def is_pythagorean_triple(a, b, c):
    """
    :param a:
        a positive integer
    :param b:
        another positive integer
    :param c:
        third positive integer
    :return:
        True if a, b, c form a Pythogorean Triple
        False otherwise
    """
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError(f"Invalid inputs {a} {b} {c}")

    numbers = [a, b, c]
    numbers.sort()
    a, b, c = numbers

    if (a ** 2 + b ** 2) == c ** 2:
        return True

    return False
