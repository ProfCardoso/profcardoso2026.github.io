---
title: Projet Python
---

# Projet Python : Mini-Maze (petit labyrinthe)

<link rel="stylesheet" href="../../assets/style.css" />


## Séance 2 : Déplacement

### Reprise du projet à partir de celui de la séance précédente

Voici le code de la séance précédente : <a href="Rendu_1.py"> Rendu 1 </a>. Vous pouvez le tester pour comparer avec votre programme.

## Fonctionnement du déplacement

Sur Pyxel, il est possible de détecter l'appui court ou long sur les touches de votre clavier/souris.

### Gestion du clavier et de la souris

#### Utilisation du Clavier

| Fonction | Descriptions |
| :---:    |:---:|
| pyxel.btn(KEY) | Touche maintenue |
| pyxel.btnp(KEY) | Appui unique |

Exemples :

```python
# Touche maintenu de -> 
pyxel.btn(pyxel.KEY_RIGHT)

# Appui unique de la barre espace
pyxel.btnp(pyxel.KEY_SPACE)
```

#### Utilisation de la Souris

Exemples :

```python
# récuperer la position de la souris
pyxel.mouse_x
pyxel.mouse_y

# détecter un clique de souris
pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
```

### Rapport

Voici un code à tester, répondre aux questions sur ce document : <a href="Rapport_2.odt"> Rapport 2 </a>.

```python
import pyxel

pyxel.init(128, 128, title="Exemple déplacement")

x = 45
y = 55
couleur = 7


def update():
    global x, y, couleur
    if pyxel.btn(pyxel.KEY_LEFT):           # btn : vrai tant que la touche est maintenue
        x = x - 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2
    if pyxel.btn(pyxel.KEY_UP):
        y = y - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        y = y + 2
    x = max(5, min(85, x))                 # on empêche le texte de sortir de la fenêtre
    y = max(5, min(120, y))
    if pyxel.btnp(pyxel.KEY_SPACE):         # btnp : vrai une seule fois, au moment de l'appui
        couleur = couleur + 1
        if couleur > 15:
            couleur = 1


def draw():
    pyxel.cls(0)
    pyxel.text(x, y, "Bouge-moi !", couleur)


pyxel.run(update, draw)
```

### Code à réaliser

Réaliser le code dont voici le cahier des charges :
- écran de 128x128, séparé en 2 couleurs ;
- un carré de taille 5x5, affiché dans la partie haute de l'écran et dont la couleur est identique à la couleur du bas ;
- le carré change de couleur en passant dans l'autre moitié de l'écran.

Voir rendu final voulu au tableau.

Bonus : Faire plusieurs "couches" de couleurs.