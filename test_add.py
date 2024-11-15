import unittest

from add import add

class Testadd(unittest.TestCase):
    def test_add(self):
        result = add.add(3, 7)
        self.assertEqual(result, 10)

        result = add.add(3, -7)
        self.assertEqual(result, -4)

        result = add.add(-3, -7)
        self.assertEqual(result, -10)
