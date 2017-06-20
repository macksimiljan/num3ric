from numpy import arange, cos, cross, dot, pi as PI, sin, array, nan as NaN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def angle_of_secure_table(f, interval):
    max_iterations = 100
    current_iteration = 0
    tolerance = 0.001
    if not is_appropriate_initial_interval(interval, f):
        print('Probably no way to get a secure table.')
        return NaN

    while abs(interval[0] - interval[1]) > tolerance and current_iteration < max_iterations:
        middle = (interval[1] + interval[0]) / 2
        height_start = diff_leg2ground_function(interval[0], f)
        height_middle = diff_leg2ground_function(middle, f)
        if height_start * height_middle < 0:
            interval[1] = middle
        else:
            interval[0] = middle
        current_iteration += 1
    return interval[0], current_iteration


def is_appropriate_initial_interval(interval, f):
    height_start = diff_leg2ground_function(interval[0], f)
    height_end = diff_leg2ground_function(interval[1], f)
    print('height start:', height_start, 'height end:', height_end)
    return height_start * height_end < 0


def z_coordinate(f, alpha, x, y):
    # plane: a*x + b*y + c*z = d
    a, b, c, d = coefficients_plane_equation(alpha, f)
    if c == 0:
        raise Exception('c = 0!')

    return 1 / c * (d - a * x - b * y)
    

def coefficients_plane_equation(alpha, f):
    p1 = array([cos(alpha), sin(alpha), f(alpha)])
    p2 = array([cos(alpha + PI / 2), sin(alpha + PI / 2), f(alpha + PI / 2)])
    p3 = array([cos(alpha + PI), sin(alpha + PI), f(alpha + PI)])
    vector1 = p3 - p1
    vector2 = p2 - p1
    # cross product is a vector (a,b,c) normal to the plane
    cross_product = cross(vector1, vector2)
    a, b, c = cross_product
    # evaluates d = a*x1 + b*x2 + c*x3
    d = dot(cross_product, p1)
    return a, b, c, d


def diff_leg2ground_function(alpha, f):
    x4 = cos(3 / 2 * PI + alpha)
    y4 = sin(3 / 2 * PI + alpha)
    z4_leg = z_coordinate(f, alpha, x4, y4)
    z4_ground = f(3 / 2 * PI + alpha)
    return z4_leg - z4_ground


def draw_diff(f):
    alphas = arange(0, 2 * PI, 0.001 * PI)
    y_axis = [diff_leg2ground_function(alpha, f) for alpha in alphas]
    plt.plot(alphas, y_axis)
    plt.show()


def draw_curve(f):
    alphas = arange(0, 2 * PI, 0.001 * PI)
    x_axis = [cos(alpha) for alpha in alphas]
    y_axis = [sin(alpha) for alpha in alphas]
    z_axis = [f(alpha) for alpha in alphas]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x_axis, y_axis, z_axis)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


def f(alpha):
    return sin(alpha) + 0.5 * cos(2*alpha)


def angle_to_degree(alpha):
    return 360 / (2 * PI) * alpha


# draw_curve(f)
# draw_diff(f)
start = 0.0*PI
end = 0.5*PI
alpha, no_iterations = angle_of_secure_table(f, [start, end])
print('interval [', start, ',', end, ']')
print(round(alpha, 3), '=', round(angle_to_degree(alpha), 3), '°')
x4 = cos(3/2 * PI + alpha)
y4 = sin(3/2 * PI + alpha)
z4_leg = z_coordinate(f, alpha, x4, y4)
z4_ground = f(3/2 * PI + alpha)
print('x4:', x4, ', y4:', y4, ' z4_leg:', z4_leg, ', z4_ground:', z4_ground)
print('#iterations:', no_iterations)
print('You have to rotate the table by {}°.'.format(round(angle_to_degree(alpha-start), 2)))