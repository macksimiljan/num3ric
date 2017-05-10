from numpy import pi as PI, sin

from numeric.e2.fixed_point_iteration import *
from numeric.e2.rotation import Rotation

print('Fixed-Point Iteration\n------------------')

values1, no_iterations1, convergent1 = fix_iter(phi1, 0.0, 1e-12, 100)
values2, no_iterations2, convergent2 = fix_iter(phi2, 0.5, 1e-12, 100)
values3, no_iterations3, convergent3 = fix_iter(phi2, 1.0, 1e-12, 100)


print('{:17}\t{:17}\t{:17}\t{:17}'.format('iteration', 'phi_1', 'phi_2', 'phi_3'))
for i in range(0, 101):
    if i < 6:
        v1 = values1[i] if i < len(values1) else values1[-1]
        v2 = values2[i] if i < len(values2) else values2[-1]
        v3 = values3[i] if i < len(values3) else values3[-1]
        print('{:^10}\t{:17.14f}\t{:17.14f}\t{:17.14f}'.format(i, v1, v2, v3))
    elif i == 6:
        print('{:^10}\t{:^17}\t{:^17}\t{:^17}'.format('...', '...', '...', '...'))
    if i == len(values1) - 1 and convergent1:
        print('{:^10}\t{:^17.14}\t{:^17}\t{:^17}'.format(i, values1[-1], '...', '...'))
    if i == len(values2) - 1 and convergent2:
        print('{:^10}\t{:^17}\t{:^17.14}\t{:^17}'.format(i, '...', values2[-1], '...'))
    if i == len(values3) - 1 and convergent3:
        print('{:^10}\t{:^17}\t{:^17}\t{:^17.14}'.format(i, '...', '...', values3[-1]))

order1 = calculate_order_of_convergence(values1[2], values1[3], values1[4], values1[-1])
order2 = calculate_order_of_convergence(values2[2], values2[3], values2[4], values2[-1])
order3 = calculate_order_of_convergence(values3[2], values3[3], values3[4], values3[-1])

print()
print('order of convergence for ... \n'
      '\t... phi_1:\t', round(order1, 2), '\n\t... phi_2:\t', round(order2, 2), '\n\t... phi_3:\t', round(order3, 2))

print_functions((-1, 2))

print()
input('Press enter ... ')
print('\nRotation\n------------------')


def function_f(x):
    return sin(x)

alpha = PI / 8
interval = (PI, 7 * PI)

rotation = Rotation(function_f, interval, alpha)
rotated_interval = rotation.get_interval_after_rotation()
rotated_x = (rotated_interval[0] + rotated_interval[1]) / 2

rotation.approximate_rotated_y(rotated_x)

point_before_rotation = rotation.get_point_before_rotation()
point_after_rotation = rotation.get_point_after_rotation()


print('alpha =', round(alpha, 4))
print('interval [a, b] = [', round(interval[0], 4), ',', round(interval[1], 4), ']')
print('interval [c, d] = [', round(rotated_interval[0], 4), ',', round(rotated_interval[1], 4), ']')
print()

print('x  = {:6.4} \t f(x)  = {:6.4}'.format(point_before_rotation[0], point_before_rotation[1]))
print('x\' = {:6.4} \t g(x\') = {:6.4}'.format(point_after_rotation[0], point_after_rotation[1]))

pyplot.figure()
pyplot.subplot(211)
x_axis = arange(interval[0], interval[1], 0.01 * PI)
pyplot.plot(x_axis, function_f(x_axis))

pyplot.subplot(212)
x_axis_rotated = arange(rotated_interval[0], rotated_interval[1], 0.01 * PI)
y_axis_rotated = [rotation.approximate_rotated_y(x) for x in x_axis_rotated]
pyplot.plot(x_axis_rotated, y_axis_rotated)

pyplot.show()
