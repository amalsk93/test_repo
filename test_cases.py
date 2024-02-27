import unittest
import numpy as np
from main import PerformNumberOperations


class TestDivisionFunction(unittest.TestCase):

    def test_does_function_give_infinity_when_divided_by_zero(self):
        expected_output = np.inf
        test_obj = PerformNumberOperations()
        test_obj.a = 10
        test_obj.b = 0
        c = test_obj.divide_two_numbers()
        self.assertEqual(c, expected_output)
