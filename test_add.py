import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(3, 7)
        self.assertEqual(result, 10)

        result = Calculator.add(3, -7)
        self.assertEqual(result, -4)

        result = Calculator.add(-3, -7)
        self.assertEqual(result, -10)
