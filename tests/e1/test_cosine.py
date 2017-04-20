from tests.context import cosine
from math import pi

import unittest


class BasicTestSuite(unittest.TestCase):
    """Test cases for resistance calculation."""

    def test_is_even(self):
        self.assertTrue(cosine.is_even(2))
        self.assertTrue(cosine.is_even(42))
        self.assertTrue(cosine.is_even(-4))
        self.assertTrue(cosine.is_even(0))

    def test_is_odd(self):
        self.assertFalse(cosine.is_even(1))
        self.assertFalse(cosine.is_even(43))
        self.assertFalse(cosine.is_even(-1))

    def test_first_member_cosine_series(self):
        self.assertEqual(1, cosine.get_member_cosine_series(0, 0))
        self.assertEqual(1, cosine.get_member_cosine_series(0, 42))

    def test_second_member_cosine_series(self):
        self.assertEqual(0, cosine.get_member_cosine_series(1, 0))
        self.assertEqual(-8, cosine.get_member_cosine_series(1, 4))
        self.assertEqual(-3.125, cosine.get_member_cosine_series(1, 2.5))

    def test_third_member_cosine_series(self):
        self.assertEqual(3.375, cosine.get_member_cosine_series(2, 3))

    def test_fourth_member_cosine_series(self):
        self.assertEqual(-64.8, cosine.get_member_cosine_series(3, 6))

    def test_first_member_cosine_series_by_factorization(self):
        self.assertEqual(1, cosine.get_member_cosine_series_by_factorization(0, 0))
        self.assertEqual(1, cosine.get_member_cosine_series_by_factorization(0, 42))

    def test_second_member_cosine_series_by_factorization(self):
        self.assertEqual(0, cosine.get_member_cosine_series_by_factorization(1, 0))
        self.assertEqual(-8, cosine.get_member_cosine_series_by_factorization(1, 4))
        self.assertEqual(-3.125, cosine.get_member_cosine_series_by_factorization(1, 2.5))

    def test_third_member_cosine_series_by_factorization(self):
        self.assertEqual(3.375, cosine.get_member_cosine_series_by_factorization(2, 3))

    def test_fourth_member_cosine_series_by_factorization(self):
        self.assertEqual(-64.8, cosine.get_member_cosine_series_by_factorization(3, 6))

    def test_cosine_as_series(self):
        self.assertEqual(1, cosine.cosine_as_series(0))
        self.assertAlmostEqual(0, cosine.cosine_as_series(pi/2), 12)
        self.assertAlmostEqual(-1, cosine.cosine_as_series(pi),12)
        self.assertAlmostEqual(0, cosine.cosine_as_series(3 * pi / 2), 12)
        self.assertAlmostEqual(1, cosine.cosine_as_series(2 * pi), 12)


if __name__ == '__main__':
    unittest.main()