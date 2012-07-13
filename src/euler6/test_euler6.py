# -*- coding: utf-8 -*-
import unittest
import euler3

class TestSumOfSquares(unittest.TestCase):

    def test_euler_announcement(self):
        result = euler3.sum_of_squares(10)
        self.assertEqual(385, result)


class TestSquareOfSums(unittest.TestCase):

    def test_euler_announcement(self):
        result = euler3.square_of_sums(10)
        self.assertEqual(3025, result)

class TestDifference(unittest.TestCase):

    def test_euler_announcement(self):
        result = euler3.difference(10)
        self.assertEqual(2640, result)

    def test_returns_right_result(self):
        result = euler3.difference(100)
        self.assertEqual(25164150, result)


if __name__ == '__main__':
    unittest.main()
