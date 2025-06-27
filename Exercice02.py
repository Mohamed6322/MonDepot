import unittest

# Fonction à tester
def puissance(a, b):
    return a ** b

# Classe de test
class TestPuissance(unittest.TestCase):
    def test_puissance(self):
        self.assertEqual(puissance(2, 3), 8)        
        self.assertEqual(puissance(5, 2), 25)        
        self.assertEqual(puissance(0, 4), 0)        
        self.assertEqual(puissance(7, 1), 7)      
        self.assertEqual(puissance(3, 3), 27)       
        self.assertEqual(puissance(-2, 2), 4)      
   
# Définition d'un objet test
test_puissance = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)

# Exécution du test
unittest.TextTestRunner().run(test_puissance)