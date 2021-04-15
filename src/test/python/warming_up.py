import unittest

from src.warming_up import find_hypotenuse


class MyTestCase(unittest.TestCase):

    def test_find_hypotenuse(self):
        self.assertEqual(find_hypotenuse(3, 4), 5)

    # def test_collect_all_unique_words(self):
    #    self.assertEqual(sum_of_numbers(179), 17)


if __name__ == '__main__':
    unittest.main()
