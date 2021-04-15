import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(5, result)

    def test_subtract(self):
        result = subtract(6, 2)
        self.assertEqual(4, result) 

    def test_divide(self):
        result = divide(10, 5)
        self.assertEqual(2, result)

    def test_multiply(self):
        result = multiply(4, 3)
        self.assertEqual(12, result)