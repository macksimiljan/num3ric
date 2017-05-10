from numeric.e2.rotation import Rotation
from numpy import matrix, arange, sin, cos, pi as PI
from matplotlib.pyplot import figure, subplot, plot, show as show_plot


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

figure(1)
subplot(211)
x_axis = arange(interval[0], interval[1], 0.01 * PI)
plot(x_axis, function_f(x_axis))

subplot(212)
x_axis_rotated = arange(rotated_interval[0], rotated_interval[1], 0.01 * PI)
y_axis_rotated = [rotation.approximate_rotated_y(x) for x in x_axis_rotated]
plot(x_axis_rotated, y_axis_rotated)


show_plot()