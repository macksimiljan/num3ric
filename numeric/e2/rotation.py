from math import sin, cos
from numpy import NaN


class Rotation(object):

    def __init__(self, function_f, interval, angle):
        self.__function_f = function_f
        self.__interval = interval
        self.__angle = angle
        self.__epsilon = 1e-6
        self.__x = NaN
        self.__y = NaN
        self.__x_rotated = NaN
        self.__y_rotated = NaN
        self.__actual_iterations = 0
        self.__function_h = self.__create_function_h()

    def __create_function_h(self):
        def h(x):
            return self.__x_rotated - x * cos(self.__angle) + self.__function_f(x) * sin(self.__angle)
        return h

    def get_point_before_rotation(self):
        return [self.__x, self.__y]

    def get_point_after_rotation(self):
        return [self.__x_rotated, self.__y_rotated]

    def get_interval_after_rotation(self):
        left = self.rotate_x(self.__interval[0])
        right = self.rotate_x(self.__interval[1])
        return [left, right]

    def approximate_rotated_y(self, x_rotated, tolerance=1e-12, max_iterations=1000):
        self.__x_rotated = x_rotated
        self.__x = self.__approximate_x(tolerance, max_iterations)
        self.__y = self.__function_f(self.__x)
        self.__y_rotated = self.__rotate_y(self.__x)
        return self.__y_rotated

    def __approximate_x(self, tolerance, max_iterations):
        self.__actual_iterations = 0
        left = self.rotate_x(self.__interval[0])
        right = self.rotate_x(self.__interval[1])
        middle = (left + right) / 2
        while abs(left - right) > tolerance and self.__actual_iterations < max_iterations:
            if self.__function_h(left) * self.__function_h(middle) <= 0:
                right = middle
            else:
                left = middle
            middle = (left + right) / 2
            self.__actual_iterations += 1
        return middle

    def rotate_x(self, x):
        return x * cos(self.__angle) - self.__function_f(x) * sin(self.__angle)

    def __rotate_y(self, x):
        return x * sin(self.__angle) + self.__function_f(x) * cos(self.__angle)
