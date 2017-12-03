import unittest
from advent2017 import spiral_mem


class TestSpiralMemory(unittest.TestCase):

    def test_one(self):
        self.assertEqual(spiral_mem(1), 0)

    def test_twelve(self):
        self.assertEqual(spiral_mem(12), 3)

    def test_twenty_three(self):
        self.assertEqual(spiral_mem(23), 2)

    def test_ten_twenty_eight(self):
        self.assertEqual(spiral_mem(1024), 31)


if __name__ == '__main__':
    unittest.main()
