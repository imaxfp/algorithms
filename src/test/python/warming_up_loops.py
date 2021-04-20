import unittest
from src.warming_up_loops import even_numbers_range, factorial, divisors_of_a_number, list_of_squares, minimal_divisor, \
    find_count_of_numbers_greater_then_index_number


class MyTestCase(unittest.TestCase):

    def test_even_numbers_range(self):
        self.assertEqual(even_numbers_range(1, 43),
                         [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(14), 87178291200)

    def test_divisors_of_a_number(self):
        self.assertEqual(divisors_of_a_number(32), [1, 2, 4, 8, 16, 32])

    def test_list_of_squares(self):
        self.assertEqual(list_of_squares(15), [1, 4, 9])

    def test_minimal_divisor(self):
        self.assertEqual(minimal_divisor(15), 3)

    def test_find_count_of_numbers_greater_then_index_number(self):
        self.assertEqual(find_count_of_numbers_greater_then_index_number([1, 2, 3, 4, 5], 0), 4)
        self.assertEqual(find_count_of_numbers_greater_then_index_number([10, 2, 3, 4, 5], 0), 0)
        self.assertEqual(find_count_of_numbers_greater_then_index_number([3, 2, 3, 10, 1], 1), 2)


if __name__ == '__main__':
    unittest.main()
