from numeric.e3.horner import *
from numeric.e3.taylor import *

# # Test case
# coefficients_test = [n for n in range(6, 0, -1)]
# horner_test = Horner(coefficients_test)
# print('k=0:\n', horner_test.calculate_horner_schema(2, 0))
# print('k=8:\n', horner_test.calculate_horner_schema(2, 8))
# print('taylor coefficients:', horner_test.taylor_coefficients(2, 6))
# print()


show_p()

show_q()

# binary number to decimal base
binary_number = ([1] * 500)
binary_number.extend([0] * 100)
binary_number.extend([1] * 100)
#binary_number = [1, 1, 0, 1, 0, 1] #test: 53
horner_binary_number = Horner(binary_number[::-1])
schema = horner_binary_number.calculate_horner_schema(2, 0)
print('decimal number: {:7.3}'.format(schema[2, -1]))

