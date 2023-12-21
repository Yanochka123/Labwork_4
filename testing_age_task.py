import unittest

from age_task import binary_search


class SudokuTestCase(unittest.TestCase):
    def test_binary_search(self):
        values = [1, 2, 3, 4]
        age = 2
        expected_number = 1
        self.assertEqual(binary_search(
            values, 0, len(values)-1, age), expected_number)

        values = [0, 10, 12, 14, 124]
        age = 12
        expected_number = 2
        self.assertEqual(binary_search(
            values, 0, len(values)-1, age), expected_number)

        values = [1, 2, 3, 5, 6, 7, 8, 9, 124]
        age = 110
        expected_number = 7
        self.assertEqual(binary_search(
            values, 0, len(values)-1, age), expected_number)


'''
    def test_get_row(self):
        puzzle = [["1", "2", "."], ["4", "5", "6"], ["7", "8", "9"]]
        pos = (0, 0)
        expected_row = ["1", "2", "."]
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(expected_row, actual_row)

        puzzle = [["1", "2", "3"], ["4", ".", "6"], ["7", "8", "9"]]
        pos = (1, 0)
        expected_row = ["4", ".", "6"]
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(expected_row, actual_row)

        puzzle = [["1", "2", "3"], ["4", "5", "6"], [".", "8", "9"]]
        pos = (2, 0)
        expected_row = [".", "8", "9"]
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(expected_row, actual_row)
'''


if __name__ == '__main__':
    unittest.main()
