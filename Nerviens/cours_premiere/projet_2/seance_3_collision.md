---
title: Projet Python
---

# Projet Python : Mini-Maze (petit labyrinthe)

<link rel="stylesheet" href="../../assets/style.css" />


## Séance 3 : Collision

### Reprise du projet à partir de celui de la séance précédente

Voici le code de la séance précédente : <a href="Rendu_2.py"> Rendu 2</a>. Vous pouvez le tester pour comparer avec votre programme.

## Détecter une collision

Une collision est détectée quand **deux objets se chevauchent à l'écran** ; Pyxel ne le fait pas pour nous, il faut le calculer à chaque image dans update.  

Chaque objet est remplacé par **son rectangle englobant**, décrit par **quatre nombres** : `x` et `y` (coin haut-gauche), `w` (largeur) et `h` (hauteur). L'axe `y` est dirigé vers le bas.

**Deux rectangles A et B ne se touchent pas si l'un des quatre cas est vrai** :

|Cas|Condition|
|:--:|:------:|
|A est à gauche de B|ax + aw <= bx|
|A est à droite de B|ax >= bx + bw|
|A est au-dessus de B|ay + ah <= by|
|A est en dessous de B|ay >= by + bh|


Il y a collision quand **aucun de ces cas n'est vrai**. En appliquant les lois de <a href="https://fr.wikipedia.org/wiki/Lois_de_De_Morgan" target="_blank">De Morgan</a>, on obtient la version utilisée en pratique :

```python
# x, y sont les positions
# w, h sont les largeurs et hauteurs
#Ici deux carrés, 1 et 2

def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    """Retourne True si deux rectangles (1 et 2) se chevauchent."""
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )
```

**Remarque :** Vous pouvez garder cette fonction bien pratique pour vos projets.

## Rapport

Voici un code à tester, répondre aux questions sur ce document : <a href="Rapport_3.odt"> Rapport 3 </a>.

```python
import pyxel

pyxel.init(128, 128, title='Collision')
# Ajout de la souris à l'écran
pyxel.mouse(True)

# Carré B
bx, by, bw, bh = 70, 50, 30, 20

# Carré A
aw, ah = 16, 16

def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return (
        ax < bx + bw and
        ax + aw > bx and
        ay < by + bh and
        ay + ah > by
    )

def update():
    # Ferme le jeu en appuyant sur la touche Q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    # Calcul de la position du carréA
    ax = pyxel.mouse_x - aw // 2
    ay = pyxel.mouse_y - ah // 2
    # Affichage du carré B
    pyxel.rect(bx, by, bw, bh, 5)
    
    # CONDITIONS
    if collision(ax, ay, aw, ah, bx, by, bw, bh):
        pyxel.rect(ax, ay, aw, ah, 8)
        pyxel.text(5, 5, 'COLLISION', 7)
    else:
        pyxel.rect(ax, ay, aw, ah, 11)

pyxel.run(update, draw)
```

## Constante

En Python, il n'existe pas de mot-clé natif pour déclarer une constante immuable ; on utilise la convention de nommage en MAJUSCULES (ex: `PI` = 3.14) pour indiquer qu'une variable ne doit pas être modifiée.


## Code à réaliser

Votre collègue développeur a commencé un petit code pour faire un jeu de course. Vous reprenez son code pour l'aider avec les collisions des murs.

```python
import pyxel

pyxel.init(128, 128, title='Murs')

joueurx = 10
joueury = 10
joueurw = 8
joueurh = 8

VITESSE = 2

murs = [(0, 128//4, 128//2, 8), (128//2, 2*(128//4), 128//2, 8), (0, 3*(128//4), 128//2, 8)]

arrivee = (128-8, 128-8, 8, 8)


def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by

def touche_un_mur(x, y, w, h, murs):
    pass

def touche_l_arrivee(x, y, w, h, arrivee):
    pass

def update():
    global joueurx,joueury,joueurw,joueurh
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    dx, dy = 0, 0
    if pyxel.btn(pyxel.KEY_LEFT):
        dx = -VITESSE
    if pyxel.btn(pyxel.KEY_RIGHT):
        dx = VITESSE
    if pyxel.btn(pyxel.KEY_UP):
        dy = -VITESSE
    if pyxel.btn(pyxel.KEY_DOWN):
        dy = VITESSE

    joueurx += dx
    joueury += dy


def draw():
    pyxel.cls(0)
    
    # Affichage des murs
    for (mx, my, mw, mh) in murs:
        pyxel.rect(mx, my, mw, mh, 5)
        
    # Affichage de l'arrivée
    ax, ay, aw, ah = arrivee
    pyxel.rect(ax, ay, aw, ah, 14)
    
    # Affichage du joueur
    pyxel.rect(joueurx, joueury, joueurw, joueurh, 11)

pyxel.run(update, draw)
```

1. Affichez les mots "collisions" et "fin" sur l'écran quand le joueur touche les murs ou l'arrivée.

2. Bonus : Ajouter des fonctionnalités pour le faire ressembler à un jeu de course :
- chronomètre
- touche reset pour recommencer la  course
- malus si obstables touchés
- etc etc ...

**Attention !** Nous allons améliorer ce code durant la prochaine séance, garder le précieusement !