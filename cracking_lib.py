from cipher_lib import *


# il existe autant de clés de chiffrement césar que la longueur de l'ensemble de caractères que l'on peut chiffrer.
def brute_force(s: str) -> list[str]:
    chaines_possibles = []
    for n in range(len(caracteres_chiffres)):
        chaines_possibles.append(chiffrement_cesar(s, n))
    return chaines_possibles


def freq_lettre(s: str, c: str) -> float:
    nb_appartitons_c = 0
    for caractere in s:
        if caractere == c:
            nb_appartitons_c += 1

    return nb_appartitons_c/len(s)


def freq_texte(s: str) -> list[float]:
    frequences = []
    for caractere in caracteres_chiffres:
        frequences.append(freq_lettre(s, caractere))
    return frequences
