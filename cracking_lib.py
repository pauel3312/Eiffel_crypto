from cipher_lib import *


# il existe autant de clés de chiffrement césar que la longueur de l'ensemble de caractères que l'on peut chiffrer.
def brute_force(s: str) -> list[str]:
    chaines_possibles = []
    for n in range(len(caracteres_chiffres)):
        chaines_possibles.append(chiffrement_cesar(s, n))
    return chaines_possibles


