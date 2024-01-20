caracteres_chiffres = "abcdefghijklmnopqrstuvwxyz"
caracteres_autorises = caracteres_chiffres + " \n'.,"


def decalage(c: str, n: int) -> str:
    if c not in caracteres_chiffres or len(c) != 1:
        return c
    indice_caractere_rendu = (caracteres_chiffres.index(c) + n) % len(caracteres_chiffres)
    return caracteres_chiffres[indice_caractere_rendu]


def chiffrement_cesar(s: str, n: int) -> str:
    chaine_chiffree = ""
    for caractere in s:
        chaine_chiffree += decalage(caractere, n)
    return chaine_chiffree


def dechiffrement_cesar(s: str, n: int) -> str:
    return chiffrement_cesar(s, -n)


def chiffrement_vigenere(s: str, k: str) -> str:
    chaine_chiffree = ""
    indice = 0

    for caractere in s:
        nb_decalage = caracteres_chiffres.index(k[indice % len(k)])

        if caractere in caracteres_chiffres:
            indice += 1
            caractere_a_ajouter = decalage(caractere, nb_decalage)
        else:
            caractere_a_ajouter = caractere

        chaine_chiffree += caractere_a_ajouter

    return chaine_chiffree


def dechiffrement_vigenere(s: str, k: str) -> str:
    cle_de_dechiffrement = ""

    for caractere in k:
        indice_de_dechiffrement = len(caracteres_chiffres) - caracteres_chiffres.index(caractere)
        indice_de_dechiffrement %= len(caracteres_chiffres)
        cle_de_dechiffrement += caracteres_chiffres[indice_de_dechiffrement]

    return chiffrement_vigenere(s, cle_de_dechiffrement)


if __name__ == "__main__":
    print(dechiffrement_vigenere(chiffrement_vigenere("nadine n'est pas un velociraptor.", "nadine"), "nadine"))
