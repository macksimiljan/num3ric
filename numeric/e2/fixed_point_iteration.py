import matplotlib.pyplot as pyplot
from numpy import arange, exp, cos, log as ln


def function_f(x):
    return x**5 + 3*x + 4


def function_g(x):
    return exp(cos(x)) + 8*x**2


def phi1(x):
    return (exp(cos(x)) - 4) / (x**4 - 8*x + 3)


def phi2(x):
    return (exp(cos(x)) - 3*x - 4) / (x**4 - 8*x)


def phi3(x):
    return (exp(cos(x)) - 3*x - 4) / (x**4 + 2*x**3 + 4*x**2) + 2


def fix_iter(F, x0, tolerance, max_iterations):
    current_iteration = 0
    x_previous = float('Infinity')
    x = x0
    values = [x0]
    while current_iteration < max_iterations and not is_convergent(x, x_previous, tolerance):
        x_previous = x
        x = F(x)
        values.append(x)
        current_iteration += 1
    return values, current_iteration, is_convergent(x, x_previous, tolerance)


def is_convergent(x, x_previous, tolerance):
    return abs(x - x_previous) < tolerance


def calculate_order_of_convergence(x_k, x_k_plus_1, x_k_plus_2, x_star):
    numerator = ln(abs(x_k_plus_1 - x_star) / abs(x_k_plus_2 - x_star))
    denominator = ln(abs(x_k - x_star) / abs(x_k_plus_1 - x_star))
    return numerator / denominator


def print_functions(interval):
    fig, ax = pyplot.subplots()
    x_axis = arange(interval[0], interval[1], 0.1)
    ax.plot(x_axis, function_f(x_axis), label='$f(x) = x^5 + 3x +4$')
    ax.plot(x_axis, function_g(x_axis), label='$f(x) = e^{\cos(x)} + 8 x^2$')
    pyplot.xlabel('$x$')
    pyplot.ylabel('$f(x)$')
    ax.legend()

    pyplot.show()