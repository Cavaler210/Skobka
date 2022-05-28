import unittest
from skobki import skobka


class TestSkobki(unittest.TestCase):
    def test_positive_sequence(self):  # тестируем правильную последовательность

        self.assertEqual(skobka("()"), skobka("()"))
        self.assertEqual(skobka(""), skobka(""))

    def test_not(self):
        self.assertEqual(skobka(")"), skobka(")"))
        self.assertEqual(skobka(")("),skobka(")("))
        self.assertEqual(skobka("(()))"),skobka("(()))"))
if __name__=="__main__":
    unittest.main()
