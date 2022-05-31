import unittest
from skobki import skobka


class TestSkobki(unittest.TestCase):
    def test_1(self):  # тестируем правильную последовательность
        self.assertEqual(skobka("()"), True)

    def test_2(self):
        self.assertEqual(skobka(""), True)

    def test_3(self):
        self.assertEqual(skobka("((()))"), True)

    def test_4(self):
        self.assertEqual(skobka(")"), False)

    def test_5(self):
        self.assertEqual(skobka("(()))"), False)

    def test_6(self):
        self.assertEqual(skobka(")()("), False)


if __name__ == "__main__":
    unittest.main()
