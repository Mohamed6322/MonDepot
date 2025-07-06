import unittest
import string_utils  

class TestStringUtils(unittest.TestCase):

    def test_est_palindrome(self):
        self.assertTrue(string_utils.est_palindrome("radar"))
        self.assertTrue(string_utils.est_palindrome("Radar"))  # casse ignorée
        self.assertFalse(string_utils.est_palindrome("bonjour"))
        self.assertTrue(string_utils.est_palindrome(""))

    def test_inverser_chaine(self):
        self.assertEqual(string_utils.inverser_chaine("abc"), "cba")
        self.assertEqual(string_utils.inverser_chaine("Radar"), "radaR")
        self.assertEqual(string_utils.inverser_chaine(""), "")

    def test_compter_voyelles(self):
        self.assertEqual(string_utils.compter_voyelles("Bonjour"), 3)  # o,u,o
        self.assertEqual(string_utils.compter_voyelles("AEIOUY"), 6)
        self.assertEqual(string_utils.compter_voyelles("bcdfg"), 0)
        self.assertEqual(string_utils.compter_voyelles(""), 0)

# Définition d’un objet test
test_utils = unittest.TestLoader().loadTestsFromTestCase(TestStringUtils)

# Exécution du test
unittest.TextTestRunner().run(test_utils)