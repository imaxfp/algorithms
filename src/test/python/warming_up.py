import unittest

from src.warming_up import find_hypotenuse, find_the_number_of_hundreds, clock, time_slot_difference, \
    find_the_max, is_leap_year


class MyTestCase(unittest.TestCase):

    def test_find_hypotenuse(self):
        self.assertEqual(find_hypotenuse(3, 4), 5)

    def test_find_the_number_of_hundreds(self):
        self.assertEqual(find_the_number_of_hundreds(1891), 8)
        self.assertEqual(find_the_number_of_hundreds(11975), 9)

    def test_clock(self):
        self.assertEqual(clock(0), (0, 0))
        self.assertEqual(clock(1), (0, 1))
        self.assertEqual(clock(1449), (0, 9))
        self.assertEqual(clock(2880), (24, 0))
        self.assertEqual(clock(28811), (0, 11))

    def test_time_slot_difference(self):
        self.assertEqual(time_slot_difference(start_h=1, start_min=1, start_sec=0,
                                              end_h=1, end_min=2, end_sec=2), 62)
        self.assertEqual(time_slot_difference(start_h=1, start_min=1, start_sec=1,
                                              end_h=2, end_min=2, end_sec=2), 3661)

    def test_find_the_max(self):
        self.assertEqual(find_the_max([1, 3, 5, 2, 1]), 5)

    def test_leap_year(self):
        self.assertEqual(is_leap_year(2007), False)
        self.assertEqual(is_leap_year(2000), True)
        self.assertEqual(is_leap_year(2021), False)
        self.assertEqual(is_leap_year(2024), True)


if __name__ == '__main__':
    unittest.main()
