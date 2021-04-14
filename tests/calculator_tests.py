import unittest
from modules import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(4, subtract(6, 2)) 

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_multiply(self):
        self.assertEqual(6, multiply(4, 3))