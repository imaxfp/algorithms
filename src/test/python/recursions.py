import unittest
from src.recursions import fibonacci_number, reverse_array_rec, add_two_numbers, letter_combinations_phone_number


class MyTestCase(unittest.TestCase):

    def test_fibonacci_number(self):
        self.assertEqual(fibonacci_number(1), 1)
        self.assertEqual(fibonacci_number(2), 1)
        self.assertEqual(fibonacci_number(3), 2)
        self.assertEqual(fibonacci_number(4), 3)
        self.assertEqual(fibonacci_number(100), 354224848179261915075)

    def test_reverse_array(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(reverse_array_rec(arr, 0, len(arr) - 1), [6, 5, 4, 3, 2, 1])

    def test_add_two_numbers(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        self.assertEqual(add_two_numbers(l1, l2), [7, 0, 8])

    def test_letter_combinations_phone_number(self):
        self.assertEqual(letter_combinations_phone_number(23), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


if __name__ == '__main__':
    unittest.main()
