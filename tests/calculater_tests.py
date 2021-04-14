import unittest
from modules import calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.assertEqual(5, add(2, 3))

    def setUp(self):
        self.assertEqual(4, subtract(6, 2)) 

    def setUp(self):
        self.assertEqual(2, divide(10, 5))

    def setUp(self):
        self.assertEqual(6, multiply(2, 3))