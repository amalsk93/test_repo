import numpy as np
import pandas as pd


class PerformNumberOperations:

    def __int__(self, first_num, second_num):
        self.a = first_num
        self.b = second_num

    def divide_two_numbers(self):
        """
        Function to divide 2 numbers
        :return: returns the quotient if divisor is non zero else returns inf
        :rtype: float
        """
        if self.b != 0:
            c = self.a / self.b
            print("The quotient is:", c)
            return c
        else:
            print("Division by Zero error")
            return np.inf


num = PerformNumberOperations()
num.a = 10
num.b = 5
num.divide_two_numbers()
