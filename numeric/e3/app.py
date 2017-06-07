from numeric.e3.horner import *


coefficients_test = [n for n in range(6, 0, -1)]
horner_test = Horner(coefficients_test)
for k in range(10):
    print(horner_test.calculate_horner_schema(2, k))
    print(horner_test.taylor_series_to_string(2, k))
    print('for k = {:d}: P({}) = {}'.format(k, 2, horner_test.calculate_value_by_taylor(2, 2, k)))
    print()

coefficients_p = [1 for n in range(41)]
coefficients_q = [n + 1 for n in range(31)]

x = 0.2

horner_p = Horner(coefficients_p)
horner_q = Horner(coefficients_q)
print(horner_p.taylor_coefficients(x, len(coefficients_p)))
for k in [10, 20, 30]:
    print('for P(x) with k = {:d}:'.format(k))
    print('\t P({}) = {}'.format(x, horner_p.calculate_value_by_taylor(x, x, k)))
    print()
