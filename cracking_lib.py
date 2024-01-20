from cipher_lib import *

frequences_theoriques_fr = [0.0840, 0.0106,
                            0.0303, 0.0418,
                            0.1726, 0.0112,
                            0.0127, 0.0092,
                            0.0734, 0.0031,
                            0.0005, 0.0601,
                            0.0296, 0.0713,
                            0.0526, 0.0301,
                            0.0099, 0.0655,
                            0.0808, 0.0707,
                            0.0574, 0.0132,
                            0.0004, 0.0045,
                            0.0030, 0.0012]

dict_lettres_frequences_theoriques = {}

for i, freq in enumerate(frequences_theoriques_fr):
    dict_lettres_frequences_theoriques[caracteres_chiffres[i]] = freq


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


def distance(l1: list, l2: list):
    if len(l1) != len(l2):
        raise Exception("les listes ne font pas la même longueur")

    distance_temp = 0
    for i in range(len(l1)):
        distance_temp += (l1[i] - l2[i])**2

    return distance_temp


def cle(s: str) -> int:
    frequences = freq_texte(s)
    min_distance = distance(frequences, frequences_theoriques_fr)
    key = 0
    for k in range(1, len(caracteres_chiffres)):
        frequences = frequences[-1:] + frequences[:-1]
        distance_temp = distance(frequences, frequences_theoriques_fr)
        if distance_temp < min_distance:
            key = k
            min_distance = distance_temp
    return key


