from numpy import arange, array, cos, cross, dot, pi as PI, sin, meshgrid, array, ravel
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def angle_of_secure_table(f):
    init_alpha = 0
    x4_init = cos(3/2 * PI + init_alpha)
    y4_init = sin(3/2 * PI + init_alpha)
    z4_leg = z_coordinate(f, init_alpha, x4_init, y4_init)
    z4_ground = f(3/2 * PI + init_alpha)

    interval_start, interval_end = 0, 90
    tolerance = 10 ** -6
    while z4_leg - z4_ground > tolerance:
        alpha_new = 0.5 * (interval_end - interval_start)
        x4 = cos(3 / 2 * PI + alpha_new)
        y4 = sin(3 / 2 * PI + alpha_new)
        z4_leg = z_coordinate(f, alpha_new, x4, y4)
        z4_ground = f(3 / 2 * PI + alpha_new)







def z_coordinate(f, alpha, x, y):
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
    cross_product = cross(vector1, vector2)
    a, b, c = cross_product
    d = dot(cross_product, p1)
    return a, b, c, d


def draw_curve():
    alphas = arange(0, 2 * PI, 0.01 * PI)
    x_axis = [cos(alpha) for alpha in alphas]
    y_axis = [sin(alpha) for alpha in alphas]
    z_axis = [sin(alpha) + 0.5*cos(2*alpha) for alpha in alphas]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x_axis, y_axis, z_axis, '-b')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


def f(alpha):
    return sin(alpha) + 0.5 * cos(2*alpha)

# draw_curve()
angle_of_secure_table(f)