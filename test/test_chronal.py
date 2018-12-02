import unittest
from advent2018 import calc_resulting_freq, calc_repeat_freq


class TestResultFreq(unittest.TestCase):

    def test_three_ones(self):
        self.assertEqual(calc_resulting_freq(["+1", "+1", "+1"]), 3)

    def test_last_neg(self):
        self.assertEqual(calc_resulting_freq(["+1", "+1", "-2"]), 0)

    def test_all_negs(self):
        self.assertEqual(calc_resulting_freq(["-1", "-2", "-3"]), -6)

class TestDoubleFreq(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(calc_repeat_freq(["+1", "-1"]), 0)

    def test_ten(self):
        self.assertEqual(calc_repeat_freq(["+3", "+3", "+4", "-2", "-4"]), 10)

    def test_five(self):
        self.assertEqual(calc_repeat_freq(["-6", "+3", "+8", "+5", "-6"]), 5)

    def test_fourteen(self):
        self.assertEqual(calc_repeat_freq(["+7", "+7", "-2", "-7", "-4"]), 14)

if __name__ == '__main__':
    unittest.main()
