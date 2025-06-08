
# ==============================================
# INF5130 - Devoir 1 - Été 2025
# Exercice 3-e : Implémentation des algorithmes
#               PIVOT() et DIAGONALE()
#
# Auteurs : Adlin Louisama,     LOUA20309509
#           Senat Lutherking,   SENL19109703
# ==============================================


def pivot(M, id, if_, jd, jf, x):
    """
    Recherche récursive d'une valeur x dans une matrice M triée ligne/colonne.

    Paramètres :
    - M : matrice d'entiers respectant les conditions (I) et (II)
    - id : indice de début des lignes
    - if_ : indice de fin des lignes
    - jd : indice de début des colonnes
    - jf : indice de fin des colonnes
    - x   : valeur entière recherchée

    Retour :
    - bool : True si x est présent dans M, False sinon
    """

    if id > if_ or jd > jf:
        return False
    if id == if_ and jd == jf:
        return M[id][jd] == x
    pi = (id + if_) // 2
    pj = (jd + jf) // 2
    if M[pi][pj] == x:
        return True
    elif x < M[pi][pj]:
        return pivot(M, id, pi, jd, pj, x) or \
               pivot(M, id, pi, pj + 1, jf, x) or \
               pivot(M, pi + 1, if_, jd, pj, x)
    else:
        return pivot(M, id, pi, pj + 1, jf, x) or \
               pivot(M, pi + 1, if_, jd, pj, x) or \
               pivot(M, pi + 1, if_, pj + 1, jf, x)
    

def dichoto(M, id, if_, jd, jf, x):
    """
    Recherche binaire de l'indice d sur la diagonale principale de la sous-matrice.

    Paramètres :
    - M : matrice d'entiers respectant les conditions (I) et (II)
    - id : indice de début des lignes
    - if_ : indice de fin des lignes
    - jd : indice de début des colonnes
    - jf : indice de fin des colonnes
    - x   : valeur entière recherchée

    Retour :
    - int : plus petit indice d tel que M[i_d + d, j_d + d] >= x
    """
    n = min(if_ - id, jf - jd) + 1
    g = 0
    d = n
    while g < d:
        m = (g + d) // 2
        if x <= M[id + m][jd + m]:
            d = m
        else:
            g = m + 1
    return g


def diagonale(M, id, if_, jd, jf, x):
    """
    Recherche récursive de x en exploitant la croissance diagonale de M.

    Paramètres :
    - M : matrice d'entiers respectant les conditions (I) et (II)
    - id : indice de début des lignes
    - if_ : indice de fin des lignes
    - jd : indice de début des colonnes
    - jf : indice de fin des colonnes
    - x   : valeur entière recherchée

    Retour :
    - bool : True si x est présent dans M, False sinon
    """
    if id > if_ or jd > jf:
        return False
    n = min(if_ - id, jf - jd) + 1
    d = dichoto(M, id, if_, jd, jf, x)
    if id + d <= if_ and jd + d <= jf and M[id + d][jd + d] == x:
        return True
    return diagonale(M, id + d, if_, jd, jd + d - 1, x) or \
           diagonale(M, id, id + d - 1, jd + d, jf, x)


# Lecture du fichier .txt contenant la matrice.
nom_fichier = input("Nom du fichier texte contenant la matrice : ").strip()
M = []

try:
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            if ligne.strip():
                M.append(list(map(int, ligne.strip().split())))
except:
    print(f"Erreur : le fichier '{nom_fichier}' est introuvable.")
    exit()

# Vérification des dimensions
n = len(M)
if n == 0:
    print("Erreur : la matrice est vide.")
    exit()

m = len(M[0])
for i in range(1, n):
    if len(M[i]) != m:
        print(f"Erreur : la ligne {i+1} ne contient pas {m} éléments.")
        exit()

# Rechercher une valeur dans la matrice indiquée
n = len(M)
m = len(M[0])
x = int(input("Valeur à rechercher : "))

# Affichage du resultat de recherche
print("pivot  :", pivot(M, 0, n - 1, 0, m - 1, x))
print("diagonale   :", diagonale(M, 0, n - 1, 0, m - 1, x))
if min(n, m) > 1:
    print("dichoto:", dichoto(M, 0, n - 1, 0, m - 1, x))
else:
    print("dichoto: -")