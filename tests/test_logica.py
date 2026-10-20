import unittest
from logica import convertir

class ConversionTests(unittest.TestCase):
    def test_mm_m(self): self.assertAlmostEqual(convertir("1000","mm","m"),1)
    def test_coma(self): self.assertAlmostEqual(convertir("2,5","m","cm"),250)
    def test_negativo(self): self.assertAlmostEqual(convertir("-10","cm","mm"),-100)
    def test_igual(self): self.assertAlmostEqual(convertir("5","cm","cm"),5)
    def test_cero(self): self.assertEqual(convertir("0","mm","m"),0)
    def test_invalidos(self):
        for valor in ["", "hola", "nan", "inf", "1.250,5"]:
            with self.subTest(valor=valor), self.assertRaises(ValueError): convertir(valor,"mm","m")
    def test_unidad(self):
        with self.assertRaises(ValueError): convertir("2","km","m")

if __name__ == "__main__": unittest.main()
