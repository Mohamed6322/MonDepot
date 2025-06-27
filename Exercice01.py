import unittest

# Fonction à tester
def multiplication(a, b):
    return a * b

# Classe de test
class TestMultiplication(unittest.TestCase):  # héritage de TestCase de unittest
    def test_multiplication(self):
        self.assertEqual(multiplication(3, 3), 9)
        self.assertEqual(multiplication(10, 8), 80)
        self.assertEqual(multiplication(5, 6), 30)
        self.assertEqual(multiplication(0, 5), 0)
       

# Définition d'un objet test
test_multiplication = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)

# Exécution du test
unittest.TextTestRunner().run(test_multiplication)