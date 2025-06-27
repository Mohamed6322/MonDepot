import unittest

# Fonction à tester
def somme_entiers_inferieurs(n):
    return sum(range(n))

# Classe de test
class TestSommeEntiersInferieurs(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme_entiers_inferieurs(0), 0)   
        self.assertEqual(somme_entiers_inferieurs(1), 0)   
        self.assertEqual(somme_entiers_inferieurs(4), 6)   
        self.assertEqual(somme_entiers_inferieurs(8), 28)  
        self.assertEqual(somme_entiers_inferieurs(12), 66) 

    def test_somme_negatif(self):
        # Cas limite : n négatif devrait retourner 0 ou lever une exception
        self.assertEqual(somme_entiers_inferieurs(-2), 0)  # sum(range(-3)) = 0

# Définition d’un objet test
test_somme = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)

# Exécution du test
unittest.TextTestRunner().run(test_somme)