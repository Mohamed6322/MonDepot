import unittest

# Fonction à tester
def factorielle(n):
    if n < 0:
        return "Erreur : n doit être positif ou nul"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Classe de test
class TestFactorielle(unittest.TestCase):
    def test_factorielle_positive(self):
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(3), 6)
        self.assertEqual(factorielle(5), 120)

    def test_factorielle_negatif(self):
        self.assertEqual(factorielle(-4), "Erreur : n doit être positif ou nul")

# Définition d’un objet test
test_factorielle = unittest.TestLoader().loadTestsFromTestCase(TestFactorielle)

# Exécution du test
unittest.TextTestRunner().run(test_factorielle)