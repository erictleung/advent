import unittest
from advent2017 import calc_checksum


class TestCheckSum(unittest.TestCase):

    def test_one(self):
        test_array = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(calc_checksum(test_array), 18)


if __name__ == '__main__':
    unittest.main()
