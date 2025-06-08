## Auteurs : Adlin Louisama

## Implémentation en Python

Ce programme implémente les algorithmes `PIVOT`, `DICHOTO` et `DIAGONALE` pour rechercher une valeur entière `x` dans une matrice 2D qui respecte les deux propriétés suivantes :
- (I) Chaque ligne est triée en ordre croissant.
- (II) Chaque colonne est triée en ordre croissant.

```bash
algo_matrice.py : script Python contenant l'implémentation.
```

---

## Exécution du programme

1. Lancer le programme dans un terminal avec :

```bash
python3 algo_matrice.py
```

## Fichiers de test

Plusieurs fichiers .txt sont fournis pour tester le programme. chaque fichier représente une matrice :

| Fichier              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `test_normal.txt`    | Matrice valide (5x7), lignes et colonnes triées.         |
| `test_carre.txt`     | Matrice carrée plus grande (10x10), conforme aux propriétés (I) et (II).    |
| `test_dimension.txt` | Cas d’erreur : matrice avec des lignes de longueurs différentes.            |
| `test_vide.txt`      | Cas d’erreur : fichier vide, sans aucune ligne ni valeur.                   |

## Exemples d'execution

```bash
    $ python3 algo_matrice.py 
    Nom du fichier texte contenant la matrice : test_normal.txt
    Valeur à rechercher : 39
    pivot  : True
    diagonale   : True
    dichoto: 4
```

```bash
    $ python3 algo_matrice.py 
    Nom du fichier texte contenant la matrice : test_normal.txt
    Valeur à rechercher : 100
    pivot  : False
    diagonale   : False
    dichoto: 5
```

```bash
    $ python3 algo_matrice.py 
    Nom du fichier texte contenant la matrice : test_vide
    Erreur : le fichier 'test_vide' est introuvable.
```

```bash
    $ python3 algo_matrice.py 
    Nom du fichier texte contenant la matrice : test_dimension.txt
    Erreur : la ligne 3 ne contient pas 7 éléments.
```