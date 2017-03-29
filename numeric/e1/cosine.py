from math import factorial
from math import cos


def cosine_from_library(x):
    return cos(x)


def cosine_as_series(x):
    cosine = 0
    current_position = 0
    while True:
        cosine_prev = cosine
        m = get_member_cosine_series(current_position, x)
        cosine += m
        current_position += 1
        if cosine == cosine_prev:
            break
    return cosine


def get_member_cosine_series(position, x):
    # position indices start with 0
    sign = 1 if is_even(position) else -1
    numerator = x ** (2 * position)
    denominator = factorial(2 * position)
    return sign * (numerator / denominator)


def is_even(number):
    return True if (number % 2 == 0) else False
