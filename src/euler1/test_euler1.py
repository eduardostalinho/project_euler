# -*- coding: utf-8 -*-
import unittest
from euler1 import sum_of_multiples

class TestSumOfMultiples(unittest.TestCase):

    def test_sum_of_multiples(self):
        '''
        You are the 225183rd person to have solved this problem.
        Let's get to the 233168!
        '''
        result = sum_of_multiples()
        self.assertEqual(233168, result)

if __name__ == '__main__':
    unittest.main()
