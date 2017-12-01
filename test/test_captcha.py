import unittest
from advent2017 import inv_captcha


class TestCaptcha(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(inv_captcha(1122), 3)

    def test_ones(self):
        self.assertEqual(inv_captcha(1111), 4)

    def test_seq(self):
        self.assertEqual(inv_captcha(1234), 0)

    def test_loop(self):
        self.assertEqual(inv_captcha(91212129), 9)


if __name__ == '__main__':
    unittest.main()
