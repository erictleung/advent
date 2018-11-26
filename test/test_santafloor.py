import unittest
from advent2015 import which_santas_floor


class TestSantaFloor(unittest.TestCase):

    def test_simple_one(self):
        self.assertEqual(which_santas_floor("(())"), 0)

    def test_simple_two(self):
        self.assertEqual(which_santas_floor("()()"), 0)

    def test_repeats_one(self):
        self.assertEqual(which_santas_floor("((("), 3)

    def test_repeats_two(self):
        self.assertEqual(which_santas_floor("(()(()("), 3)

    def test_rights(self):
        self.assertEqual(which_santas_floor("))((((("), 3)

    def test_short_negs_one(self):
        self.assertEqual(which_santas_floor("())"), -1)

    def test_short_negs_two(self):
        self.assertEqual(which_santas_floor("))("), -1)

    def test_long_negs_one(self):
        self.assertEqual(which_santas_floor(")))"), -3)

    def test_long_negs_two(self):
        self.assertEqual(which_santas_floor(")())())"), -3)

if __name__ == '__main__':
    unittest.main()
