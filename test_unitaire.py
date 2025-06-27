def addition(a, b):
    return a + b-1  # supprime -1

def test_addition():
    result = addition(3, 5)
    assert result == 7, f"le résultat attendu est 7, mais le résultat obtenu est {result}"
    result = addition(3, 9)
    assert result == 11, f"le résultat attendu est 11, mais le résultat obtenu est {result}"
test_addition()
print("Test terminé...")
# test avec des classe
import unittest

# Fonction à tester
def addition(a, b):
    return a + b

# Classe de tes
class TestAddition(unittest.TestCase):  #héritage de la class Testcase de unitest
          # definition du code dela metthode de test
    def test_addition(self):
             self.assertEqual(addition(2,3),5)
             self.assertEqual(addition(7,8),15)
             self.assertEqual(addition(9,3),12)
#defition d'un objecet test
test_addition = unittest.TestLoader().loadTestsFromTestCase(TestAddition)
# exécuté du test
unittest.TextTestRunner().run(test_addition)
