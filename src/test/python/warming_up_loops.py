import unittest

from src.warming_up_numbers import find_hypotenuse, find_the_number_of_hundreds, clock, time_slot_difference, \
    find_the_max, is_leap_year


class MyTestCase(unittest.TestCase):

    def test_find_hypotenuse(self):
        self.assertEqual(find_hypotenuse(3, 4), 5)

    def test_find_the_number_of_hundreds(self):
        self.assertEqual(find_the_number_of_hundreds(1891), 8)
        self.assertEqual(find_the_number_of_hundreds(11975), 9)


if __name__ == '__main__':
    unittest.main()
