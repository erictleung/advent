import unittest
from advent2017 import inv_captcha, half_captcha


class TestCaptcha(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(inv_captcha(1122), 3)

    def test_ones(self):
        self.assertEqual(inv_captcha(1111), 4)

    def test_seq(self):
        self.assertEqual(inv_captcha(1234), 0)

    def test_loop(self):
        self.assertEqual(inv_captcha(91212129), 9)


class TestHalfCaptcha(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(half_captcha(1212), 6)

    def test_zero(self):
        self.assertEqual(half_captcha(1221), 0)

    def test_seq(self):
        self.assertEqual(half_captcha(123425), 4)

    def test_one_two_three(self):
        self.assertEqual(half_captcha(123123), 12)

    def test_alternate_one(self):
        self.assertEqual(half_captcha(12131415), 4)


if __name__ == '__main__':
    unittest.main()
