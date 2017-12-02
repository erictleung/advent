import unittest
from advent2017 import calc_checksum, calc_even_checksum


class TestCheckSum(unittest.TestCase):

    def test_one(self):
        test_array = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(calc_checksum(test_array), 18)


class TestCheckSumEvenDiv(unittest.TestCase):

    def test_even_div(self):
        test_array = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
        self.assertEqual(calc_even_checksum(test_array), 9)


if __name__ == '__main__':
    unittest.main()
