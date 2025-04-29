import unittest
from calcr import calcular

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calcular(10, 5, '+'), 15)

    def test_subtracao(self):
        self.assertEqual(calcular(10, 5, '-'), 5)

    def test_multiplicacao(self):
        self.assertEqual(calcular(4, 3, '*'), 12)

    def test_divisao(self):
        self.assertEqual(calcular(20, 5, '/'), 4)

    def test_divisao_por_zero(self):
        self.assertEqual(calcular(10, 0, '/'), "Erro: divisão por zero!")

    def test_operacao_invalida(self):
        self.assertEqual(calcular(5, 5, '%'), "Operação inválida.")

if __name__ == "__main__":
    unittest.main()
