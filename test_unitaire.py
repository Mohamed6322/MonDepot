def addition(a, b):
    return a + b-1  # supprime -1

def test_addition():
    result = addition(3, 5)
    assert result == 7, f"le résultat attendu est 7, mais le résultat obtenu est {result}"
    result = addition(3, 9)
    assert result == 12, f"le résultat attendu est 11, mais le résultat obtenu est {result}"
test_addition()
print("Test terminé...")