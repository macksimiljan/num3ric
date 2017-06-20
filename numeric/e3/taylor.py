import matplotlib.pyplot as pyplot
from numpy import arange

from numeric.e3.horner import *

def P(x):
    sum = 0
    for n in range(0, 41):
        sum += x ** n
    return sum

def Q(x):
    sum = 0
    for n in range(0, 31):
        sum += (n + 1) * x**n
    return sum

evaluation_point = 0.2
x_values = arange(-0.2, 0.6, 0.01)


def show_p():
    horner = Horner([1] * 41)
    print('Taylorreihe:', horner.taylor_series_to_string(evaluation_point, 5), '+ ...')
    three_taylor_values = []
    for k in [10, 20, 30]:
        y_values = [horner.calculate_value_by_taylor(x, evaluation_point, k) for x in x_values]
        three_taylor_values.append(y_values)
    show_taylor(P, three_taylor_values)


def show_q():
    horner = Horner([n + 1 for n in range(31)])
    print('Taylorreihe:', horner.taylor_series_to_string(evaluation_point, 5), '+ ...')
    three_taylor_values = []
    for k in [10, 20, 30]:
        y_values = [horner.calculate_value_by_taylor(x, evaluation_point, k) for x in x_values]
        three_taylor_values.append(y_values)
    show_taylor(Q, three_taylor_values)


def show_taylor(target_function, three_taylor_values):
    pyplot.figure()
    y_values_target = [target_function(x) for x in x_values]
    for k in [1, 2, 3]:
        pyplot.subplot(310 + k)
        pyplot.plot(x_values, three_taylor_values[k - 1], label='Taylor')
        pyplot.plot(x_values, y_values_target, '--', label='Target Function')
        pyplot.legend(loc='upper right')
    pyplot.show()