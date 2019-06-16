def armstrong(number):
    """Given an integer, this function find whether or not it is an armstrong number"""

    if not isinstance(number, int):
        raise TypeError

    num = number
    sum = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        sum += (digit ** 3)
    return sum == number
