
import unittest
from soma_imposto import somaImposto

class TestSomaImposto(unittest.TestCase):
    def test_basico(self):
        self.assertAlmostEqual(somaImposto(10.0, 100.0), 110.0, places=2)
        self.assertAlmostEqual(somaImposto(17.5, 200.0), 235.0, places=2)

    def test_zero(self):
        self.assertEqual(somaImposto(0.0, 250.0), 250.0)

    def test_negativos(self):
        with self.assertRaises(ValueError):
            somaImposto(-1.0, 100.0)
        with self.assertRaises(ValueError):
            somaImposto(10.0, -50.0)

if __name__ == "__main__":
    unittest.main()
