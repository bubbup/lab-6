import unittest

# from add import Add

class Testadd(unittest.TestCase):
    def test_add(self):
        result = Add.add(3, 7)
        self.assertEqual(result, 10)

        result = Add.add(3, -7)
        self.assertEqual(result, -4)

        result = Add.add(-3, -7)
        self.assertEqual(result, -10)
