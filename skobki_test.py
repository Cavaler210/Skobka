import unittest
from skobki import skobka

class TestSkobki(unittest.TestCase):
    def test_positive_sequence(self): #тестируем правильную последовательность
        call=skobka(input()) # Вызов тестируемой функции
        result="Верная скобочная последовательность" # Ожидаемый результат
        self.assertEqual(call, result, skobka("()"))