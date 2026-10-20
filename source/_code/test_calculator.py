"""ឧទាហរណ៍ unit test សម្រាប់ម៉ាស៊ីនគិតលេខសាមញ្ញ។"""

import unittest


def add(a, b):
    """បូកលេខពីរ។"""
    return a + b


def multiply(a, b):
    """គុណលេខពីរ។"""
    return a * b


def divide(a, b):
    """ចែកលេខពីរ។ បញ្ចេញ ZeroDivisionError បើ b == 0។"""
    return a / b


class TestCalculator(unittest.TestCase):
    """សាកល្បងអនុគមន៍គណនា។"""

    def setUp(self):
        self.pairs = [(1, 2, 3), (0, 0, 0), (-1, 1, 0), (2.5, 0.5, 3.0)]

    def test_add(self):
        for a, b, expected in self.pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
