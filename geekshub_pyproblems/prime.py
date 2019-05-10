"""Given a number, the function returns whether or not it is true"""


def is_prime(number: int):
    """
    Function to check whether the number is prime

    Parameters:
    number (int): An integer that is greater than zero

    Returns:
    True, if prime
    False, otherwise
    """
    if not number or not isinstance(number, int) or number <= 1:
        return False
    if number <= 3:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# Given a number, returns the prime number that comes immediately after the number

def next_prime(number: int):
    """
    Function that returns the next prime number

    Parameters:
        number: a positive integer

    Returns:
        the prime number that follows number

    """

    if not isinstance(number, int):
        raise ValueError(f"Invalid input {number}")

    if number <= 1:
        return 2

    start_num = number + 1

    while True:
        if is_prime(start_num):
            return start_num
        start_num += 1

print(next_prime(1000))
