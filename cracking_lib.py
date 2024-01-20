from cipher_lib import *

palier_incidence = .07

frequences_theoriques_fr = [.0840, .0106,
                            .0303, .0418,
                            .1726, .0112,
                            .0127, .0092,
                            .0734, .0031,
                            .0005, .0601,
                            .0296, .0713,
                            .0526, .0301,
                            .0099, .0655,
                            .0808, .0707,
                            .0574, .0132,
                            .0004, .0045,
                            .0030, .0012]


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


def distance(l1: list, l2: list) -> float:
    if len(l1) != len(l2):
        raise Exception("les listes ne font pas la même longueur")

    distance_temp = 0
    for indice in range(len(l1)):
        distance_temp += (l1[indice] - l2[indice])**2

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


def freq_vigenere(s: str, n: int) -> str:
    textes = [""]*n

    for caractere in caracteres_ignores:
        s = s.replace(caractere, "")

    for indice, caractere in enumerate(s):
        textes[indice % n] += caractere
    cle_en_construction = ""

    for texte in textes:
        cle_en_construction += caracteres_chiffres[cle(texte)]

    return cle_en_construction


def calcul_incidence(s: str) -> float:
    resultat = 0
    for i, caractere in enumerate(caracteres_chiffres):
        ni = s.count(caractere)
        resultat += (ni*(ni-1) / (len(caracteres_chiffres)*(len(caracteres_chiffres)-1)))
    return resultat


def meilleur_incidence(s: str) -> int:
    for n in range(1, len(s)):
        texte_a_verifier = ""
        i = 0

        while n*i < len(s):
            texte_a_verifier += s[n*i]
            i += 1

        if calcul_incidence(texte_a_verifier) > palier_incidence:
            return n
