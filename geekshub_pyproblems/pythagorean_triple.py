"""Given three integers, this function returns true if the numbers are a Pythagorean Triple"""


def is_pythagorean_triple(side_a, side_b, side_c):
    """
    :param side_a:
        a positive integer
    :param side_b:
        another positive integer
    :param side_c:
        third positive integer
    :return:
        True if a, side_b, c form a Pythogorean Triple
        False otherwise
    """
    if not isinstance(side_a, int) or not isinstance(side_b, int) or not isinstance(side_c, int):
        raise ValueError(f"Invalid inputs {side_a} {side_b} {side_c}")

    numbers = [side_a, side_b, side_c]
    numbers.sort()
    side_a, side_b, side_c = numbers

    if (side_a ** 2 + side_b ** 2) == side_c ** 2:
        return True

    return False
