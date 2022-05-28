import unittest
from skobki import skobka


class TestSkobki(unittest.TestCase):
    def test_positive_sequence(self):  # тестируем правильную последовательность

        self.assertEqual(skobka("()"), "правильная последовательность")
        self.assertEqual(skobka(""), "правильная последовательность")
        self.assertEqual(skobka("((()))"), "правильная последовательность")

    def test_not(self):
        self.assertEqual(skobka(")"), "wrong")
        self.assertEqual(skobka("(()))"),"wrong")
        self.assertEqual(skobka(")()("),"wrong")


if __name__=="__main__":
    unittest.main()
