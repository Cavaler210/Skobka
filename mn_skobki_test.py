import unittest
from mn_skobki import skob


class Test_mn_skob(unittest.TestCase):
    def test_1(self):
        self.assertEqual(skob('(){}[]'), True)

    def test_2(self):
        self.assertEqual(skob('(({{[[]]}}))'), True)

    def test_3(self):
        self.assertEqual(skob('([]){}'), True)

    def test_4(self):
        self.assertEqual(skob('({)}'), False)

    def test_5(self):
        self.assertEqual(skob('(({{}}})'), False)

    def test_6(self):
        self.assertEqual(skob('}[]()'), False)


if __name__ == '__main__':
    unittest.main()
