import unittest

from src.recursions import fibonacci_number, reverse_array_rec


class MyTestCase(unittest.TestCase):

    def test_fibonacci_number(self):
        self.assertEqual(fibonacci_number(1), 1)
        self.assertEqual(fibonacci_number(2), 1)
        self.assertEqual(fibonacci_number(3), 2)
        self.assertEqual(fibonacci_number(4), 3)
        self.assertEqual(fibonacci_number(100), 354224848179261915075)

    def test_reverse_array(self):
        self.assertEqual(reverse_array_rec([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
