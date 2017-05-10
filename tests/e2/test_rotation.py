import unittest
from numpy import cos, log, pi as PI, sin

from numeric.e2.rotation import Rotation


class BasicTestSuite(unittest.TestCase):

    def f(self, x):
        return sin(x)

    interval = [PI, 7 * PI]
    angle = PI / 8
    x = 3

    def test_rotated_interval(self):

        rotation = Rotation(self.f, self.interval, self.angle)
        interval_rotated = rotation.get_interval_after_rotation()
        left_expected = self.interval[0] * cos(self.angle) - self.f(self.interval[0]) * sin(self.angle)
        right_expected = self.interval[1] * cos(self.angle) - self.f(self.interval[1]) * sin(self.angle)
        self.assertAlmostEqual(left_expected, interval_rotated[0])
        self.assertAlmostEqual(right_expected, interval_rotated[1])

    def test_point_before_rotation(self):
        expected_point_before_rotation = [self.x, self.f(self.x)]
        expected_point_after_rotation = [self.x * cos(self.angle) - self.f(self.x) * sin(self.angle),
                                         self.x * sin(self.angle) + self.f(self.x) * cos(self.angle)]

        rotation = Rotation(self.f, self.interval, self.angle)
        rotation.approximate_rotated_y(expected_point_after_rotation[0])
        actual_point_before_rotation = rotation.get_point_before_rotation()

        self.assertAlmostEqual(expected_point_before_rotation[0], actual_point_before_rotation[0])
        self.assertAlmostEqual(expected_point_before_rotation[1], actual_point_before_rotation[1])

    def test_point_after_rotation(self):
        expected_point_after_rotation = [self.x * cos(self.angle) - self.f(self.x) * sin(self.angle),
                                         self.x * sin(self.angle) + self.f(self.x) * cos(self.angle)]

        rotation = Rotation(self.f, self.interval, self.angle)
        rotation.approximate_rotated_y(expected_point_after_rotation[0])
        actual_point_after_rotation = rotation.get_point_after_rotation()

        self.assertAlmostEqual(expected_point_after_rotation[0], actual_point_after_rotation[0])
        self.assertAlmostEqual(expected_point_after_rotation[1], actual_point_after_rotation[1])


if __name__ == '__main__':
    unittest.main()