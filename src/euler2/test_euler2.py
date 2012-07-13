# -*- coding: utf-8 -*-
import unittest
import euler2

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_breaks_on_400000(self):
        fib = euler2.fibonacci()
        self.assertTrue(fib[-1] < 4000000 )
        self.assertTrue(fib[-1] + fib[-2] > 4000000)


class TestSumOfEvens(unittest.TestCase):

    def test_sum_of_evens_has_the_right_value(self):
        result = euler2.sum_of_evens_of_fib
        self.assertEqual(4613732, euler2.sum_of_evens_of_fib)


if __name__ == '__main__':
    unittest.main()
