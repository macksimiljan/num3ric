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

# coefficients_test = [n for n in range(6, 0, -1)]
# horner_test = Horner(coefficients_test)
# for k in range(10):
#     print(horner_test.calculate_horner_schema(2, k))
#     print(horner_test.taylor_series_to_string(2, k))
#     print('for k = {:d}: P({}) = {}'.format(k, 2, horner_test.calculate_value_by_taylor(2, 2, k)))
#     print()

coefficients_p = [1] * 40
coefficients_q = [n + 1 for n in range(31)]

evaluation_point = 0.2

horner_p = Horner(coefficients_p)
print(horner_p.taylor_coefficients(evaluation_point, len(coefficients_p)))
pyplot.figure()
for k in [10, 20, 30]:
    print('for P(x) with k = {:d}:'.format(k))
    print('\t P({}) = {:7.3E}'.format(evaluation_point,
                                      horner_p.calculate_value_by_taylor(evaluation_point, evaluation_point, k)))
    print()
    pyplot.subplot(310 + k / 10)
    x_values = arange(-5, 5, 0.1)
    y_values = [horner_p.calculate_value_by_taylor(x, evaluation_point, k) for x in x_values]
    y_values_p = [P(x) for x in x_values]
    pyplot.plot(x_values, y_values, 'r', linewidth=5,label="Horner")
    pyplot.plot(x_values, y_values_p, 'b', label = "P")
    pyplot.legend(loc = 'upper right')
pyplot.show()

horner = Horner(coefficients_q)
print(horner.taylor_coefficients(evaluation_point, len(coefficients_p)))
pyplot.figure()
for k in [10, 20, 30]:
    print('for P(x) with k = {:d}:'.format(k))
    print('\t P({}) = {:7.3E}'.format(evaluation_point,
                                      horner.calculate_value_by_taylor(evaluation_point, evaluation_point, k)))
    print()
    pyplot.subplot(310+k/10)
    x_values = arange(-5, 5, 0.1)
    y_values = [horner.calculate_value_by_taylor(x, evaluation_point, k) for x in x_values]
    y_values_q = [Q(x) for x in x_values]
    pyplot.plot(x_values, y_values, linewidth=5,label="Horner")
    pyplot.plot(x_values, y_values_q, label = "Q")
    pyplot.legend(loc = 'upper right')
pyplot.show()

binary_number = ([1] * 500)
binary_number.extend([0] * 100)
binary_number.extend([1] * 100)
#binary_number = [1, 1, 0, 1, 0, 1] #test: 53
horner_binary_number = Horner(binary_number[::-1])
schema = horner_binary_number.calculate_horner_schema(2, len(binary_number), complete=False)
print('decimal number: {:7.3}'.format(schema[2, -1]))

