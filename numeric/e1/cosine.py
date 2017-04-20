from math import factorial
from math import cos


def list_cosine_values(arguments):
    precision = 2
    print("{:^3}\t{:^10}\t{:^10}\t{:>4}\t{:^10}".format('k', 'argument', 'cos series', 'cos', 'rel. error'))
    print('-'*50)
    k = 0
    for arg in arguments:
        cos_series = cosine_as_series(arg)
        cos_lib = cosine_from_library(arg)
        error = abs(cos_series - cos_lib) / abs(cos_lib)
        print("{:3d}\t{:>10.2f}\t{:>10.1e}\t{:>4.0f}\t{:>10.1e}".format(k, arg, cos_series, cos_lib, error))
        k += 1


def cosine_from_library(x):
    return cos(x)


def cosine_as_series(x):
    cosine = 0
    current_position = 0
    while True:
        cosine_prev = cosine
        cosine += get_member_cosine_series_by_factorization(current_position, x)
        current_position += 1
        if abs(cosine - cosine_prev) < 1.e-8:
            break
    return cosine


def get_member_cosine_series(position, x):
    # position indices start with 0
    sign = 1 if is_even(position) else -1
    numerator = x ** (2 * position)
    denominator = factorial(2 * position)
    return sign * (numerator / denominator)


def get_member_cosine_series_by_factorization(position, x):
    # position indices start with 0
    sign = 1 if is_even(position) else -1
    product = 1
    for denominator in range(2*position, 0, -1):
        product *= (x / denominator)
    return sign * product


def is_even(number):
    return True if (number % 2 == 0) else False
