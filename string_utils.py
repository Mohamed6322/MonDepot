def est_palindrome(chaine):
    return chaine == chaine[::-1]

def inverser_chaine(chaine):
    return chaine[::-1]

def compter_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    return sum(1 for c in chaine if c in voyelles)