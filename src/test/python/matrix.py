import unittest

from src.matrix import find_row_column_max_element


class MyTestCase(unittest.TestCase):

    def test_find_max_matrix_elemnt(self):
        matrix = [[3, 1, 2],
                  [1, 3, 4],
                  [3, 3, 3]]
        self.assertEqual(find_row_column_max_element(matrix), (1, 2))
        return None


if __name__ == '__main__':
    unittest.main()
