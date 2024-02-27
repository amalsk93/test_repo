import numpy as np


class PerformNumberOperations:

    def __int__(self, first_num, second_num):
        self.a = first_num
        self.b = second_num

    def divide_two_numbers(self):
        if self.b != 0:
            c = self.a / self.b
            print("The quotient is:", c)
            return c
        else:
            print("Division by zero error")
            return np.inf


num = PerformNumberOperations()
num.a = 10
num.b = 5
num.divide_two_numbers()
