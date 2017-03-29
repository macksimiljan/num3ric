# -*- coding: utf-8 -*-

from tests.context import resistance

import unittest


class BasicTestSuite(unittest.TestCase):
    """Test cases for resistance calculation."""

    test_cases_simple_circuit = ([2], [2, 3.5, 8, 10], [2, 0, 1], [1, -5, 2])
    test_cases_circuit = ([2.5, 4, 7, 3.5], [2.5, 0, 7, 3.5], [2.5, 4, -7, 3.5])

    def test_calc_resistance_of_series_circuit(self):
        expected = [2, 23.5, 3]
        for i in range(len(self.test_cases_simple_circuit)):
            try:
                current_case = self.test_cases_simple_circuit[i]
                total = resistance.calc_resistance_of_series_circuit(*current_case)
                self.assertAlmostEqual(expected[i], total)
            except ValueError as e:
                self.assertTrue(i == 3)

    def test_calc_resistance_of_parallel_circuit(self):
        expected = [2, 280/283, 0]
        for i in range(len(self.test_cases_simple_circuit)):
            try:
                current_case = self.test_cases_simple_circuit[i]
                total = resistance.calc_resistance_of_parallel_circuit(*current_case)
                self.assertAlmostEqual(expected[i], total)
            except ValueError as e:
                self.assertTrue(i == 3)

    def test_get_total_resistance_left(self):
        expected = [4+1/68, 2+1/52, -1]
        for i in range(len(self.test_cases_circuit)):
            try:
                current_case = self.test_cases_circuit[i]
                total = resistance.get_total_resistance_left(*current_case)
                self.assertAlmostEqual(expected[i], total)
            except ValueError as e:
                self.assertTrue(i == 2)

    def test_get_total_resistance_right(self):
        expected = [3+202/285, 1+16/19, -1]
        for i in range(len(self.test_cases_circuit)):
            try:
                current_case = self.test_cases_circuit[i]
                total = resistance.get_total_resistance_right(*current_case)
                self.assertAlmostEqual(expected[i], total)
            except ValueError as e:
                self.assertTrue(i == 2)


if __name__ == '__main__':
    unittest.main()