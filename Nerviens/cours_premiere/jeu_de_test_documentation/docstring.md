---
title: Aide
---

<link rel="stylesheet" href="../../assets/style.css" />

# Les docstrings

Une **docstring (documentation string)** est une **chaîne de caractères placée au début d’une fonction, d’une classe ou d’un module** pour expliquer ce qu’il/elle fait. Elle aide à comprendre le code sans avoir à tout relire.


## Rédaction

La docstring commence juste après la déclaration de la fonction. Elle est encadrée par des triples guillemets `"`.

### Exemple : Une docstring courte 

```python
def somme_entiers(n):
    """Calcule la somme des n premiers entiers"""
    s = 0
    for i in range(n+1):
        s = s + i
    return s

```

Dans le shell (console python), on peut alors obtenir la documentation de la fonction, à l'aide de la fonction help(fonction).

```shell
>>> help(somme_entiers)
Help on function somme_entiers in module __main__:

somme_entiers(n)
    Calcule la somme des n premiers entiers

>>>      
```

### Exemple : Une docstring longue 

- Les triples guillemets
- À la ligne une description courte, puis une ligne vide
- Une explication des paramètres et du retour avec le type suivi d'une description de ce dernier
- (option) Une ou des pré-conditions pour que le code fonctionne
- Des triples guillemets

``` python
def somme_termes_suite_geo(u0, q, n):
    """
    Calcule la somme des premiers termes d'une suite géométrique
    Paramètre :
    :param u0: float - terme de rang 0
    :param q: float - raison de la suite
    :param n: int - rang du dernier terme de la somme

    Retour :
    :return: float - somme des n premiers termes de la suite

    Pré-condition :
    :pre-condition : n est un entier strictement positif q est un nombre non nul
    """
    return u0*(1-q**(n+1))/(1-q)
```

Dans le shell, on peut alors obtenir la documentation de la fonction.

``` shell
    help(somme_termes_suite_geo)
```

Les docstrings peuvent être plus longue que le code lui même.
Les docstrings permettent de décrire des cas d'utilisation d'une fonction et peuvent remplacer un énoncé.

## Application
>
> Voici plusieurs fichiers python avec des fonctions non documentées, avec des noms peu explicites (clairs). 
> - Changer le nom pour des fonctions 
> - Ajoutez une docstring longue pour chacune des fonctions
>
> Conseils : Vous pouvez executer les fonctions pour comprendre ce qu'elles font.
>
> - <a href="fonction_myst_1.py"> Fichier 1 </a>
> - <a href="fonction_myst_2.py"> Fichier 2 </a>
> - <a href="fonction_myst_3.py"> Fichier 3 </a>