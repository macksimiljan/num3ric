import matplotlib.pyplot as pyplot
from numpy import arange, sqrt

from numeric.e3.polynom_interpolation import PolynomInterpolation


def target_function(x):
    return sqrt(2*x)

def g(x):
    return -15 * (2*x)**(-3.5)

#stuetzstellen = [(1, 30), (2, 27), (3, 25), (4, 24), (5, 21)]
stuetzstellen = [(0.5, 1), (2, 2), (4.5, 3), (8, 4)]
interpolation = PolynomInterpolation(stuetzstellen)
print(interpolation.polynom_newton(3))
print(interpolation.formula_newton)

pyplot.figure()
x_axis = arange(0.5, 8, 0.01)
y_axis = [interpolation.polynom_newton(x) for x in x_axis]
pyplot.plot(x_axis, y_axis, 'b')
for stuetzstelle in stuetzstellen:
    pyplot.plot(stuetzstelle[0], stuetzstelle[1], 'r*')
pyplot.plot(x_axis, target_function(x_axis), 'r--')
pyplot.show()

pyplot.figure()
x_axis = arange(0.5, 8, 0.01)
y_axis = [g(x) for x in x_axis]
pyplot.plot(x_axis, y_axis)
pyplot.show()

