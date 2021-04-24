import unittest

from src.arrays_loops import rotate_the_array_to_the_right, get_indexes_the_sum_of_two_numbers, two_sum_problem


class MyTestCase(unittest.TestCase):

    def test_rotate_the_array_to_the_right(self):
        self.assertEqual(rotate_the_array_to_the_right([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])

    def test_two_sum_problem(self):
        """
        Input: nums = [2, 7, 11, 15], target = 9
        Output: (0, 1)
        """
        self.assertEqual(two_sum_problem([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum_problem([3, 2, 4], 6), [1, 2])


if __name__ == '__main__':
    unittest.main()
