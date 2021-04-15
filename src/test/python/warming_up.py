import unittest

from warming_up import sum_of_numbers


class MyTestCase(unittest.TestCase):

    def test_collect_all_unique_words(self):
        self.assertEqual(sum_of_numbers(179), 17)


if __name__ == '__main__':
    unittest.main()
